import pandas as pd
import numpy as np
import os

class Character():
    def __init__(self,f,world):
        self.name = f['name']
        self.background = f['background']
        self.coreskills = [f['coreskills']]
        self.secondaryskills = [f['secondaryskills']]
        self.message = "game start" 
        self.equipment = {'gold':1}
        self.size = 5
        self.speed = 5
        self.attributes = ['started']

    def __repr__(self):
        return f"{self.name} the adventurer"
           
    def get_charData(self):
        #try to pass more on the server side. Don't pass info to the client unless there is .js that needs it. 
        return {
            'name':self.name,
            'message':self.message,
            'size':self.size,
            'speed':self.speed,
            'attributes':self.attributes
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
        c.caste = "noble"
        t = np.random.choice([t for t in world.towns if 'capitol' in str(t)])
        c.birthplace = t.name
        c.location = [t.x,t.y]
        c.equipment['gold'] += 100
        c.message = f"You begin your adventure in {str(t)} </br> Your nobile family has ties with {t.speaker}. "

    if c.background == 'Pesant family':
        c.caste = "pesant"
        t = np.random.choice([t for t in world.towns if 'town' in str(t)])
        c.birthplace = t.name
        c.location = [t.x,t.y]
        c.message = f"You wake up on the streets of {str(t)}."
        
    if c.background == 'Temple orphan':
        c.caste = "pesant"
        t = np.random.choice([t for t in world.towns if 'town' in str(t)])
        c.birthplace = t.name
        c.location = [t.x,t.y]
        c.message = f"You wake up on the streets of {str(t)}."

    if c.background == 'Nomad family':
        c.caste = "pesant"
        l = world.get_filtered_chord(t=['mountain','land'])
        c.birthplace = "the wilderness"
        c.location = l
        c.message = f"You wake up in the wilderness, {str(world.df_features.loc[c.get_location_key(),'terrain'])}."
        
#creating the character from the userform (f)
#returns a world, not a character
def create_character(character_dict,world):
    c = Character(character_dict,world)
    set_char_origin(c,world)
    world.Character = c
    
    return world
