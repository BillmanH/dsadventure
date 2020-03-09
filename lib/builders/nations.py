import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

n_init_clusters = 30
def cluster_nations(world):
    cities = world.df_features[world.df_features["terrain"] == "town"]
    world.nations = []
    world.df_features["nation number"] = np.nan
    world.df_features["nation"] = np.nan
    #     world.df_features["nation number"] = world.df_features["nation number"].
    k = KMeans(init="k-means++", n_clusters=world.culture.n_nations, n_init=n_init_clusters).fit(
        cities[["x", "y"]]
    )
    world.nations_k = k
    predict_nations(world)
    world.nations = [
        Nation(world, cluster=True, k=i) for i in np.unique(world.nations_k.labels_)
    ]
    return k


def predict_nations(world):
    world.df_features["nation number"] = world.nations_k.predict(
        world.df_features[["x", "y"]]
    )


class Nation:
    def __init__(self, world, **kwargs):
        self.name = self.name_nation(world)
        if kwargs.get("cluster", None):
            # Kmeans is the default (when the world is created)
            # Requires the integer value used when creating the world.
            self.cast_nation(world, kwargs.get("k"))
        self.diplomacy = {}
        self.capitol = None

    def cast_nation(self, world, k):
        world.df_features.loc[
            world.df_features["nation number"] == k, "nation"
        ] = self.name

    def name_nation(self, world):
        nation_name = world.culture.townNameGenerator()
        return nation_name


    def __repr__(self):
        return f"Nation of {self.name}"

    def set_capitol(self, world):
        ts = self.get_all_towns(world)
        cap = [
            t for t in ts if len(t.population) == max([len(t.population) for t in ts])
        ][0]
        cap.type = "capitol"
        self.capitol = cap
        
    def get_capitol(self, world):
        ts = self.get_all_towns(world)
        cap = [t for t in ts if t.type == "capitol"][0]
        return cap

    def get_all_towns(self, world):
        all_towns = world.df_features.loc[
            (world.df_features["nation"] == self.name)
            & (world.df_features["terrain"] == "town"),
            "feature",
        ].unique()
        return [t for t in world.towns if t.name in all_towns]

    def get_random_town(self):
        return np.random.choice(self.towns)

    def getRuler(self):
        if self.ruler:
            return self.ruler
        else:
            return None

    def get_deplomacy_df(self):
        d = pd.DataFrame(self.diplomacy).T.reset_index(drop=False)
        d["nation"] = self.name
        d.columns = ["neighbor", "favor", "stance", "nation"]
        return d[["nation", "neighbor", "favor", "stance"]]

def appoint_ruler(world, n, people):
    t = n.get_capitol(world)
    n.ruler = people.Person(world, role=f"ruler of {n.name}", location=t.key)


# nation = Nation(world,k=0)
# print(nation)

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
                if j.name not in i.diplomacy.keys():
                    i.diplomacy[j.name]={}
                if 'favor' not in i.diplomacy[j.name].keys():
                    i.diplomacy[j.name]['favor'] = .6
                i.diplomacy[j.name]['favor'] += a
                if i.diplomacy[j.name]['favor'] < 0:
                    i.diplomacy[j.name]['favor'] = .01
                if i.diplomacy[j.name]['favor'] > 1:
                    i.diplomacy[j.name]['favor'] = 1
                i.diplomacy[j.name]['stance'] = set_treaties(i.diplomacy[j.name]['favor'])

#events
def place_building(world,a,o,event):
    for n in a:
        t = np.random.choice(n.get_all_towns(world))
        t.add_building(event.key)
    return t

def place_feature(world,a,o,event):
    for n in a:
        key = world.get_filtered_chord(n=n.name,r='key')
        world.df_features.loc[key,'feature'] = event.key
        #TODO do something with e (effect amount)
        return world.df_features.loc[key,'terrain']
