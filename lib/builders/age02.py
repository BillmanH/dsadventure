import numpy as np
import pandas as pd


def labelNations(k):
    t = town([1,1],1)
    nations = {}
    for n in np.unique(k):
        nations[n] = t.townNameGenerator()
    return nations

def assignNation(x,landscape):
    nationName = landscape['nations'].get(x,np.nan)
    return nationName

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
        
    def personNameGenerator(self):
        return (np.random.choice(nameparts['1']) + \
                np.random.choice(nameparts['2']) + \
                np.random.choice(nameparts['3'])
               ).capitalize()
    
    def setLoyaltytoCrown(self):
        if 'ruler' in self.role:
            self.loyalty = 1
            
    
