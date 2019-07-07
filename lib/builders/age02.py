import numpy as np
import pandas as pd

def keyChord(key):
    '''
    takes a key "1,1", returns a coord [1,1]
    '''
    coord = key.split(":")
    return [int(coord[0]),int(coord[1])]

prefixes = pd.read_excel('../lib/Datasets/townNames.xlsx',sheet_name='prefix')['Settlement name (part 1)'].tolist()
suffixes = pd.read_excel('../lib/Datasets/townNames.xlsx',sheet_name='suffix')['Settlement name (part 2)'].tolist()
#TODO: Namegen has bug that can't convert blank values to str. Change to import as STR not NaN.
nameparts = pd.read_csv('../lib/Datasets/namegen.csv')

def labelNations(k):
    t = town([1,1],1)
    nations = {}
    for n in np.unique(k):
        nations[n] = t.townNameGenerator()
    return nations

def assignNation(x,landscape):
    nationName = landscape['nations'].get(x,np.nan)
    return nationName

class person:
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
            
class town:
    def townNameGenerator(self):
        return (np.random.choice(prefixes) + \
                np.random.choice(suffixes)
               ).capitalize().replace("\''","")
                
    def __init__(self,coord,year):
        self.x = coord[0]
        self.y = coord[1]
        self.key = f"{str(coord[0])}:{str(coord[1])}"
        self.pop = 1
        self.name = self.townNameGenerator()
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
