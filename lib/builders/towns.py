import numpy as np
import pandas as pd

class town:
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