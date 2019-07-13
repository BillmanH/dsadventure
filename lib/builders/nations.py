import numpy as np
import pandas as pd

#ML Libraries
from sklearn.cluster import KMeans

def assignNation(x,world):
    nationName = world.nations.get(x,np.nan)
    return nationName

def labelNations(k,culture):
    """
    lables a list of nations from a k-means cluster
    """
    nations = {}
    for n in np.unique(k.labels_):
        nations[n] = culture.townNameGenerator()
    return nations,k

def cluster_nations(world):
    cities = world.df_features[world.df_features['terrain']=='town']
    k_means = KMeans(init='k-means++', n_clusters=world.culture.n_nations, n_init=10)
    k_means.fit(cities[['x','y']])
    #once the labels are ready you can fetch the nation names:
    nations = labelNations(k_means,world.culture)
    return nations

def predict_nations(k_means,world):
    df = world.df_features
    predicted_nations = k_means.predict(df.loc[(df['terrain']!='ocean')]
                                        [['x','y']]
                                       )
    df.loc[(df['terrain']!='ocean'),'nation number'] = predicted_nations
    
    df['nation'] = df['nation number'].apply(lambda x: assignNation(x,world))
    return world.df_features

class Nation:
    def __init__(self,name,world):
        self.name = name
        self.towns = self.addTowns(world.towns)
        self.diplomacy = self.addDiplomacy(world.nations)
        self.ruler = self.appointRuler()
        
    def __repr__(self):
        return f"nation of {self.name}"
       
    def addTowns(self,towns):
        self.towns = [town for town in towns 
                         if town.diplomacy.get('nation','none')==self.name]
        
    def getCapitol_str(self,towns):
        c = [t.name for t in towns if t.type == 'capitol']
        return c[0]

    def getRuler_str(self):
        return self.ruler.name
    
    def getRuler(self):
        return self.ruler
    
    def addDiplomacy(self,nations):
        self.diplomacy = {}
        otherNations = [n for n in nations.values() if n != self.name]
        for o in otherNations:
            self.diplomacy[o] = {'favor':0,'stance':'neutral'} 
            
    def appointRuler(self,person):
        t = self.getCapitol_str(self.towns)
        self.ruler = person(f'ruler of {self.name}',t)
        
    def getRandomCity(self):
        return np.random.choice(self.towns)