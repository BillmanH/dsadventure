import pandas as pd
import numpy as np

class Person:
    def __init__(self,culture,role='commoner',location=None):
        self.name = culture.personNameGenerator()
        self.role = role
        self.nation = location
        self.location = location
        self.loyalty = .5
        #temperment determines the 'viciousness' of a person's decisons
        self.temperment = np.round_(np.random.random_sample(),2)        
        self.setLoyaltytoCrown()
        self.attributes = ['alive']
        self.messages = ['Hello stranger.']

    def __repr__(self):
        return f"{self.name} the {self.role}"
    
    def get_person_data(self):
        d = {'name':self.name,
            'role':self.role,
            'loyalty':self.loyalty,
            'temperment':self.temperment,
            'attributes':self.attributes,
            'messages':self.messages}
        return d
    
    def setLoyaltytoCrown(self):
        if 'ruler' in self.role:
            self.loyalty = 1
    
    def add_message(self,m):
        self.messages.append(m)

    def remove_message(self,m):
        self.messages = [i for i in self.messages if m not in i]


