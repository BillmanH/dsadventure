import pandas as pd
import numpy as np

class Person:
    def __init__(self,culture,role='peon',location=None):
        self.name = culture.personNameGenerator()
        self.role = role
        self.nation = location
        self.location = location
        self.loyalty = .5
        #temperment determines the 'viciousness' of a person's decisons
        self.temperment = np.round_(np.random.random_sample(),2)        
        self.setLoyaltytoCrown()
        
    def __repr__(self):
        return f"{self.name} the {self.role}"
    
    def get_person_data(self):
        d = {'name':self.name,
            'role':self.role,
            'loyalty':self.loyalty,
            'temperment':self.temperment}
        return d
    
    def setLoyaltytoCrown(self):
        if 'ruler' in self.role:
            self.loyalty = 1
            
