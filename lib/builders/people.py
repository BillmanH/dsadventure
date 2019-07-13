import pandas as pd
import numpy as np

class Person:
    def __init__(self,role,location):
        self.name = self.personNameGenerator()
        self.role = role
        self.nation = location
        self.location = location
        self.loyalty = .5
        #temperment determines the 'viciousness' of a person's decisons
        self.temperment = np.random.random_sample()
        
        self.setLoyaltytoCrown()
        
    def __repr__(self):
        return f"{self.name}, {self.role}, residing in {self.nation}"
    
    def setLoyaltytoCrown(self):
        if 'ruler' in self.role:
            self.loyalty = 1
            
    