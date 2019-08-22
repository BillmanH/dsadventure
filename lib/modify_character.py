import pandas as pd
import numpy as np
import os

def update_charData(char,charData):
    char.arriveFrom = charData['arriveFrom']
    char.composure = charData['composure']
    char.location = charData['location']
    char.attributes = charData['attributes']
    char.title = charData['title']
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
        self.coreskills = [f['coreskills']]
        self.secondaryskills = [f['secondaryskills']]
        self.message = "game start" 
        self.equipment = {'gold':1}
        self.size = 5
        self.speed = 15
        self.composure = 10
        self.attributes = ['started']
        self.location = None

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
            'composure':self.composure
        }

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
        c.birthplace = t.name
        c.title = f"Honerable court of {t.speaker}"
        c.location = [t.x,t.y]
        c.equipment['gold'] += 100
        c.message = f"You begin your adventure in {str(t)} </br> Your nobile family has ties with {t.speaker}. "

    if c.background == 'Pesant family':
        t = np.random.choice([t for t in world.towns if 'town' in str(t)])
        c.birthplace = t.name
        c.location = [t.x,t.y]
        c.title = f"Pesant"
        c.message = f"You wake up on the streets of {str(t)}."
        
    if c.background == 'Temple orphan':
        t = np.random.choice([t for t in world.towns if 'town' in str(t)])
        c.birthplace = t.name
        c.location = [t.x,t.y]
        c.title = f"Orphan"
        c.message = f"You wake up on the streets of {str(t)}."

    if c.background == 'Nomad family':
        l = world.get_filtered_chord(t=['mountain','land'])
        c.birthplace = "the wilderness"
        c.location = l
        c.title = f"Ranger"
        c.message = f"You wake up in the wilderness, {str(world.df_features.loc[c.get_location_key(),'terrain'])}."
        
#creating the character from the userform (f)
#returns a world, not a character
def create_character(character_dict,world):
    c = Character(character_dict,world)
    set_char_origin(c,world)
    world.Character = c
    
    return world
