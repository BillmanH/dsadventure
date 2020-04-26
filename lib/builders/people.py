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
        # opinion_of_player (-/+) determines the likelyhood that the person will do anything for player.
        self.opinion_of_player = 0
        self.born_in = self.set_born_in(world)
        self.setLoyaltytoCrown()
        self.attributes = ["alive"]
        self.messages = ["Hello stranger."]
        self.type = "person"
        # current activities of the person
        self.doing = 'nothing'
        self.finishdate = None
        world.people.append(self)

    def __repr__(self):
        return f"{self.name} the {self.role}"

    def set_born_in(self, world):
        t_born = world.df_features.loc[self.location, "terrain"]
        print(self.location, t_born)
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
            key = world.get_filtered_chord(
                t=world.landscape.land_types, r="key")
            return key

    def get_person_data(self):
        d = {
            "name": self.name,
            "role": self.role,
            "loyalty": self.loyalty,
            "temperment": self.temperment,
            "opinion_of_player": self.opinion_of_player,
            "attributes": self.attributes,
            "messages": "|".join(self.messages),
            "doing": self.doing,
            "type": "person"
        }
        return d

    def start_task(self, task, finishdate, stop_current=True):
        '''
        stop_current : boolian, do nothing if set to False
        '''
        if (self.doing == 'nothing') | stop_current:
            self.doing = task
            self.finishdate = finishdate

    def stop_task(self):
        self.doing = 'nothing'
        self.finishdate = None

    def check_complete(self, world):
        if self.finishdate:
            if self.finishdate < world.year:
                self.doing = 'nothing'
                return True
            else:
                return False
        else:
            return False

    def setLoyaltytoCrown(self):
        if "ruler" in self.role:
            self.loyalty = 1
        else:
            self.loyalty = 0.5

    def shift_opinion_of_player(self, n):
        self.opinion_of_player += n

    def add_message(self, m):
        self.messages.append(m)

    def remove_message(self, m):
        self.messages = [i for i in self.messages if m not in i]
