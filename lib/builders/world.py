import numpy as np
import pandas as pd


def mask_unknown(world):
    """
    returns updated ('masked') df_features
    hide all terrain and nations that the character has not seen.
    """
    df = world.df_features

    def masker(x):
        if (x.visited >= 1) | (x.aware >= 1):
            return x
        else:
            x.terrain = 'unknown'
            x.nation = 'unknown'
            x.feature = 'unknown'
            x['nation number'] = '0'
        return x
    df = df.apply(masker, axis=1)
    return df


def get_town(towns, name):
    t = [town for town in towns if town.name == name]
    if len(t) == 0:
        return None
    if len(t) == 1:
        return t[0]
    else:
        return t


def keycoord(key):
    '''
    takes a key "1:1", returns a coord [1,1]
    '''
    coord = key.split(":")
    return [int(coord[0]), int(coord[1])]


def coordkey(coord):
    '''
    takes a coord [1,1], returns key "1:1"
    '''
    key = ":".join([str(i) for i in coord])
    return key


def get_character_context(world, context):
    """
    gets the text of the situation facing the character right now,
    used in core view
    """
    if 'monsters' in context['terrData'].keys():
        threat = f"Danger! there are {', and'.join([n[0]['name']+'s' for n in context['terrData']['monsters']])} nearby."
    else:
        threat = "The area is calm and peaceful."

    message = threat
    return message


def get_features_or_NA(world, coord):
    try:
        l = world.df_features.loc[
            coordkey([
                int(coord[0]), int(coord[1])
            ])
        ].fillna("none").to_dict(),
    except:
        l = [{"terrain": "void"}]
    return l[0]


def set_ecology(x, landscape):
    if x.terrain == "ocean":
        return x.terrain
    if x.terrain == "mountain":
        return x.terrain
    if x.rainfall > landscape.forest_threshold:
        return "forest"
    if x.rainfall < landscape.desert_threshold:
        return "desert"
    return x.terrain


def get_area_data(world):
    """
    note: requires Character
    """
    mapData = {}
    coord = world.Character.location
    key = world.Character.get_location_key()
    mapData = {'area': world.df_features.loc[key].fillna("none").to_dict(),
               'NArea': get_features_or_NA(world, [coord[0], coord[1]-1]),
               'SArea': get_features_or_NA(world, [coord[0], coord[1]+1]),
               'EArea': get_features_or_NA(world, [coord[0]+1, coord[1]]),
               'WArea': get_features_or_NA(world, [coord[0]-1, coord[1]]),
               'meta': {'year': world.year, 'season': world.season}
               }
    return mapData


class World:
    def __init__(self, landscape):
        self.landscape = landscape
        # geopolitics is set in the second eara
        self.culture = None
        self.people = []
        self.towns = []
        self.nations = []
        self.land_shifts = []
        self.peaks = []
        self.year = 0
        self.season = 'spring'

        self.grid_elevation = self.build_blank_grid(landscape)
        self.grid_rainfall = self.build_blank_grid(landscape)
        self.df_features = pd.DataFrame()

    def tranquilize_area(self, trophies, oldLocation):
        reduction = len(trophies)/10
        self.df_features.loc[oldLocation, 'danger'] -= reduction

    def keycoord(self, key):
        '''
        takes a key "1:1", returns a coord [1,1]
        '''
        coord = key.split(":")
        return [int(coord[0]), int(coord[1])]

    # little builders (like mountains)
    def getMountain(self, height=2):
        a = [[height]]
        for i in range(height - 1, 0, -1):
            a = np.pad(a, ((1, 1), (1, 1)), 'constant', constant_values=i)
        return pd.DataFrame(a)

    def get_random_direction(self):
        direction = [1, 0, -1]
        return np.array([np.random.choice(direction),
                         np.random.choice(direction)])

    def get_next_coord(self, coord):
        nextcoord = np.add(coord, self.get_random_direction())
        return nextcoord

    def get_random_chord(self, t=None):
        df = self.grid_elevation
        x = np.random.choice(df.index.tolist(), 1)[0]
        y = np.random.choice(df.columns.tolist(), 1)[0]
        coord = [x, y]
        return np.array(coord)

    def get_filtered_chord(self, t=None, f=None, n=None, r='coord'):
        """
        t = must be an list of acceptable land types
        f = feature (if left at None it will only search NA values)
        n = must ba a nation
        r = 'coord' or 'key'
        will return a key 'x:y' that meets filtered criteria 
        """
        df = self.df_features.copy()
        if n:
            df = df[df['nation'] == n]
        if t:
            df = df[df['terrain'].isin(t)]
        if f:
            df = df[df['feature'].isin(t)]
        if f == False:
            df = df[df['feature'].isnull()]
        key = np.random.choice(df.index.tolist())
        l = df.loc[key]
        if r == 'coord':
            return [l.x, l.y]
        elif r == 'key':
            return key

    def reindexMountain(self, c, m):
        m.index = np.pad([c[0]], (round(len(m.index)/2), round(len(m.index)/2)),
                         'linear_ramp', end_values=(c[0]-round(len(m.index)/2),
                                                    c[0]+round(len(m.index)/2)
                                                    )
                         )
        m.columns = np.pad([c[1]], (round(len(m.columns)/2), round(len(m.columns)/2)),
                           'linear_ramp',
                           end_values=(c[1]-round(len(m.columns)/2),
                                       c[1]+round(len(m.columns)/2)
                                       )
                           )
        return m

    # drunkards walk that sets a mountain in a place, then drags it randomly across the map
    def brownian_land(self):
        df_new = self.grid_elevation
        for n in range(self.landscape.drop_iter):
            coord = self.get_random_chord()
            self.peaks.append(coord)
            for m in range(self.landscape.spread_iter):
                # if moutain goes off the map, it is ignored.
                try:
                    coord = self.get_next_coord(coord)
                    m = self.getMountain(height=abs(
                        int(np.round(
                            np.random.normal(self.landscape.mt_avg, self.landscape.mt_std))
                            )))
                    mdf = self.reindexMountain(coord, m)
                    df_new = df_new.add(mdf.reindex_like(df_new).fillna(0))
                    # TODO: add dfnew to dict in an array for visualization
                except:
                    continue
        self.grid_elevation = df_new

    def brownian_rainfall(self):
        df_new = self.build_blank_grid(self.landscape)
        for n in range(self.landscape.rain_iter):
            coord = self.get_random_chord()
            for m in range(self.landscape.rain_spread):
                try:
                    coord = self.get_next_coord(coord)
                    m = self.getMountain(height=abs(
                        int(np.round(
                            np.random.normal(self.landscape.mt_avg, self.landscape.mt_std))
                            )))
                    mdf = self.reindexMountain(coord, m)
                    df_new = df_new.add(mdf.reindex_like(df_new).fillna(0))
                except:
                    continue
        self.grid_rainfall = df_new

    # the world starts here with a blank canvas
    def build_blank_grid(self, landscape):
        return pd.DataFrame(columns=range(landscape.grid[1]), index=range(landscape.grid[0])).fillna(0)

    # the last step in world generation is building a dataframe of the features
    def meltMap(self, df, value='value'):
        mapdata = df.melt()
        mapdata.columns = ['y', value]
        mapdata['x'] = df.unstack().index.codes[1]
        mapdata['key'] = mapdata['x'].apply(
            str) + ":" + mapdata['y'].apply(str)
        mapdata.index = mapdata['key']
        return mapdata.drop(['key'], axis=1)

    def landTypes(self, x):
        if x <= self.landscape.water_level:
            return 'ocean'
        if x >= self.landscape.mountain_level:
            return 'mountain'
        else:
            return 'plain'

    def build_df_features(self):
        df = self.meltMap(self.grid_rainfall, value='rainfall').rename(
            columns={'value': 'water'})
        df['key'] = df.index
        df['x'] = df['key'].apply(lambda x: int(str(x).split(":")[0]))
        df['y'] = df['key'].apply(lambda x: int(str(x).split(":")[1]))
        df['elevation'] = self.meltMap(self.grid_elevation)['value']
        df['terrain'] = df['elevation'].apply(lambda x: self.landTypes(x))
        self.df_features = df

    #  Adding towns and to features map
    def add_features(self, features):
        """
        all features require both a key and a name in order to be placed on the map
        at this time only one feature per location is allowed
        existing feature is autmatcially overwritten
        """
        df = self.df_features
        for f in features:
            df.loc[f.key, 'feature'] = f.name
            df.loc[f.key, 'terrain'] = f.type

    # the surface is shifted by a small random variable.
    def shift_terrain(self):
        ter_shift = pd.DataFrame([[int(n) for n
                                   in np.round(
            np.random.normal(
                self.landscape.N_loc,
                self.landscape.N_std,
                len(self.grid_elevation.columns)))
        ]
            for r in self.grid_elevation.index]
        )
        self.grid_elevation = self.grid_elevation.add(ter_shift)

    # a single mountain is added
    def add_mountain(self, mdf):
        # mdf == a df of a mountain
        self.grid_elevation = self.grid_elevation.add(
            mdf.reindex_like(self.grid_elevation).fillna(0))

    # world politics and diplomacy
    def get_world_diplomacy(self):
        nations = self.nations
        diplomacy = pd.concat([n.get_deplomacy_df()
                               for n in nations], sort=False).reset_index(drop=True)
        return diplomacy


def appoint_ruler(world, nation):
    pass


def get_people_where_char_has_visited(world):
    """
    returns a dictionary of {{"town":[<obj>],"people":[<obj>]}
    filtered to where the character has been. 
    """
    where_the_char_has_been = world.df_features.loc[(world.df_features['visited'] == 1) &
                                                    (world.df_features['terrain'] == 'town')].dropna()
    towns_and_people = [{"town": T,
                         "people": [t for t in T.get_population(world)]}
                        for T in world.towns if T.name in np.unique(where_the_char_has_been['feature'])]
    return towns_and_people


def get_relationships_node_map(world):
    nodes = [{'name': r['town'].name,
              'title':str(r['town']).split(":")[0],
              'nation':r['town'].nation,
              'population':len(r['town'].get_population(world)),
              'type':r['town'].type,
              'location':r['town'].key,
              'founded year':r['town'].founded,
              'children': [p.get_person_data() for p in r['people']]}
             for r in get_people_where_char_has_visited(world)]
    return nodes


def get_relationships_all(world):
    nodes = get_relationships_node_map(world)
    nations = [s['nation'] for s in nodes]
    return [{'nation': i, 'children': [t for t in nodes if t['nation'] == i]} for i in nations]


def get_all_nodes(world):
    where_the_char_has_been = world.df_features.dropna()
    people = [{'name': str(t), 'type': 'person'} for t in world.people]
    nations = [{'name': str(t), 'type': 'nation'} for t in world.nations]
    towns = [{'name': f"{t.type} of {t.name}", 'type': 'town'}
             for t in world.towns]
    return towns + nations + people


def get_all_nodes(world):
    people = [{'id': str(t), 'type': 'person'} for t in world.people]
    nations = [{'id': str(t), 'type': 'nation'} for t in world.nations]
    towns = [{'id': f"{t.type} of {t.name}", 'type': 'town'}
             for t in world.towns]
    return towns + nations + people


def get_all_links(world):
    all_links = []
    town_links = [[all_links.append({'source': str(n), 'target': f"{t.type} of {t.name}"})
                   for t in n.get_all_towns(world)] for n in world.nations]
    people_links = [[all_links.append({'source': f"{n.type} of {n.name}", 'target': str(
        t)}) for t in n.get_population(world)] for n in world.towns]
    return all_links


def get_nodes_and_links(world):
    return {'nodes': get_all_nodes(world),
            'links': get_all_links(world)}
