import pandas as pd
import numpy as np

class Person:
    def __init__(self, world, culture=None, role="commoner", location=None):
        if culture:
            culture = culture
        else:
            culture = world.culture
        self.name = culture.personNameGenerator()
        self.role = role
        self.location = self.set_location(location, world)
        self.born_location = self.location
        self.loyalty = 0.5
        # temperment determines the 'viciousness' of a person's decisons
        self.temperment = np.round_(np.random.random_sample(), 2)
        self.born_in = self.set_born_in(world)
        self.setLoyaltytoCrown()
        self.attributes = ["alive"]
        self.messages = ["Hello stranger."]
        self.type = "person"
        world.people.append(self)

    def __repr__(self):
        return f"{self.name} the {self.role}"

    def set_born_in(self, world):
        t_born = world.df_features.loc[self.location, "terrain"]
        print(self.location,t_born)
        if t_born == 'town':
            return world.df_features.loc[self.location, "feature"]
        else:
            if self.role == "commoner":
                self.role = "wanderer"
            return world.df_features.loc[self.location, "terrain"]

    def set_location(self, location, world):
        if location:
            return location
        else:
            key = world.get_filtered_chord(t=world.landscape.land_types, r="key")
            return key

    def get_person_data(self):
        d = {
            "name": self.name,
            "role": self.role,
            "loyalty": self.loyalty,
            "temperment": self.temperment,
            "attributes": self.attributes,
            "messages": self.messages,
        }
        return d

    def setLoyaltytoCrown(self):
        if "ruler" in self.role:
            self.loyalty = 1
        else:
            self.loyalty = 0.5

    def add_message(self, m):
        self.messages.append(m)

    def remove_message(self, m):
        self.messages = [i for i in self.messages if m not in i]