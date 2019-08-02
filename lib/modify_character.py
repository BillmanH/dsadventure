import pandas as pd
import numpy as np
import os

class Character():
    def __init__(self,f,world):
        self.name = f['name']
        self.background = f['background']
        self.coreskills = [f['coreskills']]
        self.secondaryskills = [f['secondaryskills']]
        
    def __repr__(self):
        return f"{self.name} the adventurer"
    
    def get_charData(self):
        #try to pass more on the server side. Don't pass info to the client unless there is .js that needs it. 
        return {
            'name':self.name
        }
    
    def get_location_key(self):
        l = self.location
        return f"{(l[0])}:{l[1]}"
        
    def get_location_dict(self):
        l = self.location
        return {'x':l[0],'y':l[1]}

def char_origin(c,world):
    # a noble is born and raised in a capitol
    if c.background == 'Noble family':
        c.caste = "noble"
        t = np.random.choice([t for t in world.towns if 'capitol' in str(t)])
        c.birthplace = t.name
        c.location = [t.x,t.y]
    if c.background == 'Pesant family':
        c.caste = "pesant"
        t = np.random.choice([t for t in world.towns if 'town' in str(t)])
        c.birthplace = t.name
        c.location = [t.x,t.y]
    if c.background == 'Temple orphan':
        c.caste = "pesant"
        t = np.random.choice([t for t in world.towns if 'town' in str(t)])
        c.birthplace = t.name
        c.location = [t.x,t.y]
    if c.background == 'Nomad family':
        c.caste = "pesant"
        l = world.get_filtered_chord(t=['mountain','land'])
        c.birthplace = "the wilderness"
        c.location = l

        
#creating the character from the userform (f)
#returns a world, not a character
def create_character(character_dict,world):
    c = Character(character_dict,world)
    char_origin(c,world)
    world.Character = c
    
    return world
