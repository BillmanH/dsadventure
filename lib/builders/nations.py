import numpy as np
import pandas as pd

class nation:
    def __init__(self,name):
        self.name = name
        self.towns = []
        self.diplomacy = {}
        self.ruler = 'none'
        
    def __repr__(self):
        return f"nation of {self.name}"
    
    def addTowns(self,towns):
        self.towns = [town for town in towns 
                         if town.diplomacy.get('nation','none')==self.name]
        
    def getCapitol_str(self):
        c = [t.name for t in self.towns if t.type == 'capitol']
        return c[0]

    def getRuler_str(self):
        return self.ruler.name
    
    def getRuler(self):
        return self.ruler
    
    def addDiplomacy(self,nations):
        otherNations = [n for n in nations.values() if n != self.name]
        for o in otherNations:
            self.diplomacy[o] = {'favor':0,'stance':'neutral'} 
            
    def appointRuler(self):
        t = self.getCapitol_str()
        self.ruler = person(f'ruler of {self.name}',t)
        
    def getRandomCity(self):
        return np.random.choice(self.towns)
