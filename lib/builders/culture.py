import numpy as np
import pandas as pd

#TODO: Namegen has bug that can't convert blank values to str. Change to import as STR not NaN.

class Names:
    def __init__(self):
        self.nameparts = pd.read_csv('../lib/Datasets/namegen.csv')
        self.prefixes = pd.read_excel('../lib/Datasets/townNames.xlsx',sheet_name='prefix')['Settlement name (part 1)'].tolist()
        self.suffixes = pd.read_excel('../lib/Datasets/townNames.xlsx',sheet_name='suffix')['Settlement name (part 2)'].tolist()

default_params = {}

class Culture:
    """
    Culture are the parameters for everything that affects people, cities, nations and politics.
    """
    def __init__(self, params=default_params, ):
        #the number of nations
        self.n_nations = params.get('n_nations',8)
        #overal age of the 'civilized era' (age of unconflicted growth)
        self.eons = params.get('eons',10)
        #the number of towns spawned per iteration
        self.town_spawn = params.get('town_spawn',1)
        #the likelyhood a town will increase in size
        self.town_birthrate = params.get('town_birthrate',.3)
        #the default loyalty that a town has for it's nation at the beginning
        self.town_national_fielty = 1
        
        #names are hard cast at the moment
        self.names = Names()
    
    #  Name generation is used by many objects, so it is included in cluture.
    def townNameGenerator(self):
        """
        
        requires names.py module
        """
        return (np.random.choice(self.names.prefixes) + \
                np.random.choice(self.names.suffixes)
               ).capitalize().replace("\''","")