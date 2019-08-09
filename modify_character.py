import pandas as pd
import numpy as np
import os

from forms import playerCharacterForm as p

class Character():
    def __init__(f,world):
        self.name = f.name
        self.coreskills = [f.coreskills]
        
#creating the character from the userform (f)
def create_character_dict(f):
    character = {}
    bg = dict(p.backgroundChoices)
    return bg
