import pandas as pd
import numpy as np
import os

from .updaters.character_message import update_char_message

def update_charData(world,charData):
    char = world.Character
    char.arriveFrom = charData['arriveFrom']
    char.composure = charData['composure']
    #coerce values to int 
    l = charData['location'].split(":") 
    char.location = [int(l[0]),int(l[1])]
    #update attributes that may or may not have changed
    char.attributes = charData['attributes']
    char.title = charData['title']
    char.message = update_char_message(world)
    if 'meta' in charData.keys():
        charData['meta']['n_turns']+=1
    else:
        charData['meta'] = {}
        charData['meta']['n_turns'] = 1
    return char

class Character():
    def __init__(self,f,world):
        self.name = f['name']
        self.background = f['background']
        self.languages = []
        self.coreskills = [f['coreskills']]
        self.secondaryskills = [f['secondaryskills']]
        self.message = "game start" 
        self.title = "adventurer"
        self.equipment = {'gold':1}
        self.size = 5
        self.speed = 15
        self.composure = 10
        self.attributes = ['started']
        self.location = None
        self.arriveFrom = "Center"
        self.turn_number = 1

    def __repr__(self):
        return f"{self.name} the adventurer"
           
    def get_charData(self):
        #try to pass more on the server side. Don't pass info to the client unless there is .js that needs it. 
        return {
            'name':self.name,
            'message':self.message,
            'size':self.size,
            'speed':self.speed,
            'attributes':self.attributes,
            'location':self.get_location_key(),
            'title':self.title,
            'composure':self.composure,
            'arriveFrom':self.arriveFrom,
            'equipment':self.equipment
        }
    
    def characterSpeaksLanguage(self,world):
        #Determintes that the character speeks the language in the place where they are.
        #returns TRUE or FALSE
        return world.df_features.loc[self.get_location_key()]['nation'] in world.Character.languages

    def get_location_key(self):
        l = self.location
        return f"{(l[0])}:{l[1]}"
        
    def get_location_dict(self):
        l = self.location
        return {'x':l[0],'y':l[1]}

def set_char_origin(c,world):
    # a noble is born and raised in a capitol
    if c.background == 'Noble family':
        t = np.random.choice([t for t in world.towns if 'capitol' in str(t)])
        c.birthNation = t.nation
        c.birthTown = t.name
        c.languages.append(t.nation)
        c.title = f"Honerable court of {t.speaker}"
        c.location = [t.x,t.y]
        c.equipment['gold'] += 100
        world.df_features.loc[world.df_features['nation']==t.nation,'aware'] = 1 
        c.message = f"You begin your adventure in {str(t)} </br> Your nobile family has ties with {t.speaker}. "

    if c.background == 'Pesant family':
        t = np.random.choice([t for t in world.towns if 'town' in str(t)])
        c.birthTown = t.name
        c.birthNation = t.nation
        c.languages.append(t.nation)
        c.location = [t.x,t.y]
        c.title = f"Pesant"
        c.message = f"You wake up on the streets of {str(t)}."
        
    if c.background == 'Temple orphan':
        t = np.random.choice([t for t in world.towns if 'town' in str(t)])
        c.birthTown = t.name
        c.birthNation = t.nation
        c.location = [t.x,t.y]
        c.languages.append(t.nation)
        c.title = f"Orphan"
        c.message = f"You wake up on the streets of {str(t)}."

    if c.background == 'Nomad family':
        l = world.get_filtered_chord(t=['mountain','land'])
        c.birthTown = "the wilderness"
        c.birthNation = "none" 
        c.location = l
        c.title = f"Ranger"
        c.message = f"You wake up in the wilderness, {str(world.df_features.loc[c.get_location_key(),'terrain'])}."
        
def set_starting_eq(c,world):
    if "fencing" in c.coreskills:
        c.equipment['weapons'] = [{'name':'basic sword',
                                    'id':'0000',
                                    'quantiy':1,
                                    'range':30,
                                    'damage':6,
                                    'damage_mod':2}]
    if "archery" in c.coreskills:
        c.equipment['weapons'] = [{'name':'basic bow',
                                    'id':'0000',
                                    'quantity':20,
                                    'range':200,
                                    'damage':3,
                                    'damage_mod':1}]
    if "spellcasting" in c.coreskills:
        c.equipment['spells'] = [{'name':'lightning',
                                    'id':'0000',
                                    'quantity':4,
                                    'range':10000,
                                    'damage':8,
                                    'damage_mod':3}]

def set_skills(world,character_dict):
    skill = character_dict['secondaryskills']
    if skill == 'mountaneer':
        world.df_features.loc[world.df_features['terrain']=='mountain','aware'] = 1
    if skill == 'desert survival':
        world.df_features.loc[world.df_features['terrain']=='desert','aware'] = 1
    if skill == 'hunting':
        world.Character.equipment['food'] = [{'rations':3}]
    if skill == 'additional language':   
        world.Character.languages.append(np.random.choice([n.name for n in world.nations if n.name != world.Character.birthNation]))
    
        
        
#creating the character from the userform (f)
#returns a world, not a character
def create_character(character_dict,world):
    c = Character(character_dict,world)
    world.df_features.loc[:,'aware'] = 0
    set_char_origin(c,world)
    set_starting_eq(c,world)

    world.Character = c
    set_skills(world,character_dict)
    world.df_features['visited'] = 0
    world.df_features.loc[world.Character.get_location_key(),'visited'] = 1
    world.df_features.loc[world.df_features['terrain']=='ocean','aware'] = 1
    #automatically speaks the language of that nation
    world.Character.languages.append(world.df_features.loc[world.Character.get_location_key()].nation)
    return world
