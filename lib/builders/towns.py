import numpy as np
import pandas as pd


def get_town_dict(world,town_name):
    town_data = {'name':town_name}
    town = get_town(world.towns,town_name)
    town_data['str'] = str(town)
    town_data['diplomacy'] = town.diplomacy
    town_data['nation'] = town.nation
    town_data['type'] = town.type
    town_data['population'] = [p.get_person_data() for p in town.population]
    return town_data  
    
class Town:
    def townNameGenerator(self,names):
        """
        requires names.py module
        """
        return (np.random.choice(names.prefixes) + \
                np.random.choice(names.suffixes)
               ).capitalize().replace("\''","")
                
    def __init__(self,coord,year,culture,people):
        self.x = coord[0]
        self.y = coord[1]
        self.key = f"{str(coord[0])}:{str(coord[1])}"
        self.pop = 1
        self.name = culture.townNameGenerator()
        self.founded = year
        self.diplomacy = {}
        self.nation = self.name
        self.type = 'town'
        #the speaker is a member of the population, but also an important role in the town. 
        self.speaker =  people.Person(culture,role=f'Speaker of {self.name}',location=self.name)
        self.population = [self.speaker]
        self.culture = culture
        
    def __repr__(self):
        return f"{self.type} of {self.name}: population: {self.pop} location: [{self.x},{self.y}] founded {self.founded}"
        
    def population_growth(self, birthrate,people):
        if np.random.uniform()<birthrate:
            self.pop += 1
            self.population.append(people.Person(self.culture,role=f'peon',location=self.name))

    def haveDiplomacy(self,towns):
        for i in towns:
            print(town.nation)
            
    def set_starting_fielty(self,world):
            self.diplomacy['nation'] = world.df_features.loc[world.df_features['feature']==self.name,'nation'].values[0]
            self.diplomacy['national fealty'] = world.culture.town_national_fielty
            self.nation = self.diplomacy['nation']

def keyChord(key):
    '''
    takes a key "1,1", returns a coord [1,1]
    '''
    coord = key.split(":")
    return [int(coord[0]),int(coord[1])]

def build_towns(world,people):
    df = world.df_features
    towns = []
    for i in range(world.culture.eons):
        for s in range(int(np.round(np.random.normal(2, 1)))):
            key = np.random.choice(df[df['terrain']!='ocean'].index)
            towns.append(Town(keyChord(key),i,world.culture,people))

        for t in towns:
            t.population_growth(world.culture.town_birthrate,people)
    return towns

def get_town(towns,name):
    t = [town for town in towns if town.name == name]
    if len(t) == 0:
        return None
    if len(t) == 1:
        return t[0]
    else:
        return t
