import numpy as np
import pandas as pd

#ML Libraries
from sklearn.cluster import KMeans

def getNation(nations,a):
    return [n for n in nations if n.name ==a][0]

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
    def __init__(self,name,world,culture,people):
        self.name = name
        self.towns = self.addTowns(world.towns)
        self.diplomacy = self.addDiplomacy(world.nations)
        self.ruler = people.Person(culture,role=f'Ruler of the nation of {self.name}',location=self.get_capitol().name)
        self.get_capitol().population.append(self.ruler)
        
        
    def __repr__(self):
        return f"Nation of {self.name}"
       
    def addTowns(self,towns):
        towns = [town for town in towns 
                 if town.diplomacy.get('nation','none')==self.name]
        return towns
        
    def get_capitol(self):
        c = [t for t in self.towns if t.type == 'capitol'][0]
        return c
    
    def get_random_town(self):
        return np.random.choice(self.towns)

    def getRuler_str(self):
        return self.ruler.name
    
    def getRuler(self):
        return self.ruler
    
    def addDiplomacy(self,nations):
        diplomacy = {}
        otherNations = [n for n in nations.values() if n != self.name]
        for o in otherNations:
            diplomacy[o] = {'favor':.8,'stance':'peace'}
        return diplomacy
    
    def get_deplomacy_df(self):
        d = pd.DataFrame(self.diplomacy).T.reset_index(drop=False)
        d['nation'] = self.name
        d.columns = ['neighbor','favor','stance','nation']
        return d[['nation','neighbor','favor','stance']]
            
    def appointRuler(self,person):
        t = self.getCapitol_str(self.towns)
        self.ruler = person(f'ruler of {self.name}',t)


# Politics !!
treaties = pd.DataFrame([['sworn enemies',0],
           ['war',.1],
           ['tense',.3],
           ['peace',.6],
           ['allies',.9]], columns = ['stance','favor'])

def set_treaties(f):
    return treaties.loc[treaties[treaties['favor']<f]['favor'].idxmax()].stance
    
def alter_favor(s,o,a):
    """
    s = the target nation(s) (obj or list). s will not change. O's favor of s will change.
    o = the nation(s) (obj or list) who's favor is change. O's favor of s will change
    
    Examples:
    (a,[o]) each nation in o's favor of a is changed by s
    (a,o) o's favor of a is changed by s
    ([a],o) o's favor of each nation in a is changed by s
    s = amount of change (int)
    
    national relationship with itself doesn't decay, but town and person loyalty can.
    """
    if type(o) != list:
        o = [o]       
    for i in o:
        if type(s)!=list:
            s = [s]
        for j in s:
            if i!=j:   
                i.diplomacy[j.name]['favor'] += a
                if i.diplomacy[j.name]['favor'] < 0:
                    i.diplomacy[j.name]['favor'] = .01
                if i.diplomacy[j.name]['favor'] > 1:
                    i.diplomacy[j.name]['favor'] = 1
                i.diplomacy[j.name]['stance'] = set_treaties(i.diplomacy[j.name]['favor'])

#events
def place_building(a,o,event):
    for n in a:
        t = np.random.choice(n.towns)
        print(t.buildings)
        t.add_building(event.key)
    return t

def place_feature(world,a,o,event):
    for n in a:
        key = world.get_filtered_chord(n=n.name,r='key')
        world.df_features.loc[key,'feature'] = event.key
        #TODO do something with e (effect amount)
        return world.df_features.loc[key,'terrain']
