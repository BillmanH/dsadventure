import numpy as np
import pandas as pd


def modify_context(world, context):
    # the entire context can be modified here to add elements to the town
    town = get_town(world.towns, context['mapData']['area']['feature'])
    # copy the context object
    newcontext = context.copy()
    newcontext['n_ter_items'] = []
    for t in context['n_ter_items']:
        if t['detail']['name'] == 'building':
            t['detail']['abundance'] = len(town.get_population(world))
            t['detail']['density'] = world.year-town.founded
            newcontext['n_ter_items'].append(t)
        else:
            newcontext['n_ter_items'].append(t)
    town_data = town.get_town_data(world)
    town_data['str'] = str(town)
    newcontext['terrData']['town'] = town_data
    if world.Character.characterSpeaksLanguage(world):
        for p in newcontext['terrData']['town']['people']:
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
        # TODO: Make self.pop into a method
        self.x = coord[0]
        self.y = coord[1]
        self.key = f"{str(coord[0])}:{str(coord[1])}"
        self.name = world.culture.townNameGenerator()
        self.founded = year
        self.diplomacy = {}
        self.nation = self.name
        self.type = "town"
        # the speaker is a member of the population, but also an important role in the town.
        self.speaker = self.appoint_speaker(world, people)
        self.culture = world.culture
        self.buildings = ["great_hall"]
        world.df_features.loc[self.key, 'terrain'] = 'town'
        world.df_features.loc[self.key, 'feature'] = self.name
        

    def __repr__(self):
        return f"{self.type} of {self.name}. Location: [{self.key}]. Founded {self.founded} </br>In the nation of {self.nation}"

    def get_surrounding_area(self,world):
        coord = world.keycoord(self.key)
        surrounding_area = world.df_features.loc[(world.df_features['x'].isin([coord[0],coord[0]+1,coord[0]-1]))&(world.df_features['y'].isin([coord[1],coord[1]+1,coord[1]-1]))]
        return surrounding_area
    
    def get_birthrate(self,world):
        birthrate = 1 - self.get_surrounding_area(world)['danger'].mean()
        return birthrate

    def get_town_data(self, world):
        if self.get_surrounding_area(world)['danger'].mean()>.45:
            self.add_message_to_people(world, f"{self.name} is so dangerous! Won't anyone help us?" , onlyMessage=True)
        else:
            self.add_message_to_people(world, f"Thank you {world.Character.name}!" , onlyMessage=True)
        p = [person.get_person_data(world) for person in self.get_population(world)]
        d = {
            "name": self.name,
            "speaker": self.speaker.get_person_data(world),
            "founded": self.founded,
            "population": len(self.get_population(world)),
            "people": p,
            "key": self.key,
            "nation": self.nation,
            "loyalty": np.mean([pi['loyalty'] for pi in p]),
            "temperment": np.mean([pi['temperment'] for pi in p]),
            "danger": self.get_surrounding_area(world)['danger'].mean(),
            "buildings": self.buildings,
            "diplomacy": self.diplomacy,
            "type": self.type
        }
        return d

    def get_population(self, world):
        return [p for p in world.people if p.location == self.key]

    def appoint_speaker(self, world, people):
        return people.Person(world, role=f"Speaker of {self.name}", location=self.key)

    def population_growth(self, world, people):
        if np.random.uniform() < self.get_birthrate(world):
            people.Person(world, location=self.key)

    def population_gen(self, world, people):
        if np.random.uniform() < world.culture.town_birthrate:
            people.Person(world, location=self.key)

    def set_starting_fielty(self, world):
        self.diplomacy["nation"] = world.df_features.loc[
            world.df_features["feature"] == self.name, "nation"
        ].values[0]
        self.diplomacy["national fealty"] = world.culture.town_national_fielty
        self.nation = self.diplomacy["nation"]

    def add_building(self, b):
        self.buildings.append(b)

    def add_message_to_people(self,world, message,role=None, onlyMessage=True):
        for p in self.get_population(world):
            if message not in p.get_messages(world):
                p.add_message(message, onlyMessage=True)


def build_towns(world, people):
    df = world.df_features
    towns = []
    for i in range(world.culture.eons):
        for s in range(int(np.round(np.random.normal(2, 1)))):
            key = np.random.choice(df[df['terrain'] != 'ocean'].index)
            towns.append(Town(world.keycoord(key), world.year, world, people))
            world.year += 1
        for t in towns:
            t.population_gen(world, people)
    return towns


def get_town(towns, name):
    t = [town for town in towns if town.name == name]
    if len(t) == 0:
        return None
    if len(t) == 1:
        return t[0]
    else:
        return t

