import numpy as np
import pandas as pd

def modify_context(world,context):
    #the entire context can be modified here to add elements to the town
    town = get_town(world.towns,context['mapData']['area']['feature'])
    #copy the context object
    newcontext = context.copy()
    newcontext['n_ter_items'] = []
    for t in context['n_ter_items']:
        if t['detail']['name'] == 'building':
            t['detail']['abundance'] = town.pop
            t['detail']['density'] = world.culture.eons-town.founded
            newcontext['n_ter_items'].append(t)
        else:
            newcontext['n_ter_items'].append(t)
    town_data = {'name':context['mapData']['area']['feature']}
    town_data['str'] = str(town)
    town_data['diplomacy'] = town.diplomacy
    town_data['nation'] = town.nation
    town_data['type'] = town.type
    newcontext['terrData']['town'] = town_data
    newcontext['terrData']['people'] = [p.get_person_data() for p in town.population]
    if world.Character.characterSpeaksLanguage(world):
        for p in newcontext['terrData']['people']:
            for m in p['messages']:
                m = world.culture.gibberishGenerator(l=len(m))
    return newcontext  
    
class Town:
    def townNameGenerator(self, names):
        """
        requires names.py module
        """
        return (
            (np.random.choice(names.prefixes) + np.random.choice(names.suffixes))
            .capitalize()
            .replace("''", "")
        )

    def __init__(self, coord, year, world, people):
        #TODO: Make self.pop into a method
        self.x = coord[0]
        self.y = coord[1]
        self.key = f"{str(coord[0])}:{str(coord[1])}"
        self.pop = 1
        self.name = world.culture.townNameGenerator()
        self.founded = year
        self.diplomacy = {}
        self.nation = self.name
        self.type = "town"
        # the speaker is a member of the population, but also an important role in the town.
        self.speaker = self.appoint_speaker(world, people)
        self.population = [self.speaker]
        self.culture = world.culture
        self.buildings = ["great_hall"]
        world.df_features.loc[self.key,'terrain']='town'
        world.df_features.loc[self.key,'feature']=self.name

    def __repr__(self):
        return f"{self.type} of {self.name}: population: {self.pop} location: [{self.x},{self.y}] founded {self.founded}"
    
    def get_population(self,world):
        return [p for p in world.people if p.location == self.key]

    def appoint_speaker(self, world,people):
        return people.Person(world, role=f"Speaker of {self.name}", location=self.key)

    def population_growth(self, world, people):
        if np.random.uniform() < world.culture.town_birthrate:
            self.pop += 1
            self.population.append(people.Person(world, location=self.key))

    def set_starting_fielty(self, world):
        self.diplomacy["nation"] = world.df_features.loc[
            world.df_features["feature"] == self.name, "nation"
        ].values[0]
        self.diplomacy["national fealty"] = world.culture.town_national_fielty
        self.nation = self.diplomacy["nation"]

    def add_building(self, b):
        self.buildings.append(b)
        

def build_towns(world,people):
    df = world.df_features
    towns = []
    for i in range(world.culture.eons):
        for s in range(int(np.round(np.random.normal(2, 1)))):
            key = np.random.choice(df[df['terrain']!='ocean'].index)
            towns.append(Town(world.keycoord(key),i,world,people))

        for t in towns:
            t.population_growth(world,people)
    return towns

def get_town(towns,name):
    t = [town for town in towns if town.name == name]
    if len(t) == 0:
        return None
    if len(t) == 1:
        return t[0]
    else:
        return t
