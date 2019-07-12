import numpy as np
import pandas as pd


class Town:
    def townNameGenerator(self,names):
        """
        requires names.py module
        """
        return (np.random.choice(names.prefixes) + \
                np.random.choice(names.suffixes)
               ).capitalize().replace("\''","")
                
    def __init__(self,coord,year,names):
        self.x = coord[0]
        self.y = coord[1]
        self.key = f"{str(coord[0])}:{str(coord[1])}"
        self.pop = 1
        self.name = self.townNameGenerator(names)
        self.founded = year
        self.diplomacy = {}
        self.nation = self.name
        self.type = 'town'
        
    def __repr__(self):
        return f"{self.type} of {self.name}: population: {self.pop} location: [{self.x},{self.y}] founded {self.founded}"
    
    def population_growth(self, birthrate):
        if np.random.uniform()<birthrate:
            self.pop += 1

    def haveDiplomacy(self,towns):
        for i in towns:
            print(town.nation)

def keyChord(key):
    '''
    takes a key "1,1", returns a coord [1,1]
    '''
    coord = key.split(":")
    return [int(coord[0]),int(coord[1])]

def build_towns(world,culture,names):
    df = world.df_features
    towns = []
    for i in range(culture.eons):
        for s in range(int(np.round(np.random.normal(2, 1)))):
            key = np.random.choice(df[df['terrain']!='ocean'].index)
            towns.append(Town(keyChord(key),i,names))

        for t in towns:
            t.population_growth(culture.town_birthrate)
    return towns

def get_town(towns,name):
    t = [town for town in towns if town.name == name]
    if len(t) == 0:
        return None
    if len(t) == 1:
        return t[0]
    else:
        return t

