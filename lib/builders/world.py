import numpy as np
import pandas as pd

def keyChord(key):
    '''
    takes a key "1,1", returns a coord [1,1]
    '''
    coord = key.split(":")
    return [int(coord[0]),int(coord[1])]

#TODO: Namegen has bug that can't convert blank values to str. Change to import as STR not NaN.
nameparts = pd.read_csv('../lib/Datasets/namegen.csv')

class World:
    def __init__(self,landscape):
        self.landscape = landscape
        #geopolitics is set in the second eara
        self.geopolitics = None
        self.land_shifts = []
        self.peaks = []

        self.grid_elevation = self.build_blank_grid(landscape) 
        self.grid_rainfall = self.build_blank_grid(landscape)
        self.df_features = pd.DataFrame()

    #little builders (like mountains)
    def getMountain(self,height=2):
        a = [[height]]
        for i in range(height - 1, 0, -1):
            a = np.pad(a, ((1, 1), (1, 1)), 'constant', constant_values=i)
        return pd.DataFrame(a)

    def get_random_direction(self):
        direction = [1,0,-1]
        return np.array([np.random.choice(direction),
            np.random.choice(direction)])

    def get_next_coord(self,coord):
        nextcoord = np.add(coord,self.get_random_direction())
        return nextcoord

    def get_random_chord(self):
        df = self.grid_elevation
        x = np.random.choice(df.index.tolist(),1)[0]
        y = np.random.choice(df.columns.tolist(),1)[0]
        coord = [x,y]
        return np.array(coord)

    def reindexMountain(self,c,m):
        m.index = np.pad([c[0]],(round(len(m.index)/2)
                   ,round(len(m.index)/2)),
                    'linear_ramp',end_values=(c[0]-round(len(m.index)/2),
                    c[0]+round(len(m.index)/2)
                     )
          )
        m.columns = np.pad([c[1]],(round(len(m.columns)/2)
                   ,round(len(m.columns)/2)),
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
                    mdf = self.reindexMountain(coord,m)
                    df_new = df_new.add(mdf.reindex_like(df_new).fillna(0))
                    # TODO: add dfnew to dict in an array for visualization
                except:
                    continue
        self.grid_elevation = df_new

    def brownian_rainfall(self):
        df_new = self.grid_elevation
        for n in range(self.landscape.rain_iter):
            coord = self.get_random_chord()
            for m in range(self.landscape.rain_spread):
                try:
                    coord = self.get_next_coord(coord)
                    m = self.getMountain(height=abs(
                                            int(np.round(
                                                np.random.normal(self.landscape.mt_avg, self.landscape.mt_std))
                                                  )))
                    mdf = self.reindexMountain(coord,m)
                    df_new = df_new.add(mdf.reindex_like(df_new).fillna(0))
                except:
                    continue
        self.grid_rainfall = df_new

    # the world starts here with a blank canvas
    def build_blank_grid(self,landscape):
        return pd.DataFrame(columns=range(landscape.grid[1]),index=range(landscape.grid[0])).fillna(0)

    # the last step in world generation is building a dataframe of the features
    def meltMap(self, df,value='value'):
        mapdata = df.melt()
        mapdata.columns = ['y',value]
        mapdata['x'] = df.unstack().index.codes[1]
        mapdata['key'] = mapdata['x'].apply(str) + ":" + mapdata['y'].apply(str)
        mapdata.index = mapdata['key']
        return mapdata.drop(['key'], axis=1)

    def landTypes(self,x):
        if x<=self.landscape.water_level:
            return 'ocean'
        if x>=self.landscape.mountain_level:
            return 'mountain'
        else:
            return 'land'
    
    def build_df_features(self):
        df = self.meltMap(self.grid_rainfall,value='rainfall').rename(columns={'value':'water'})
        df['key'] = df.index
        df['x'] = df['key'].apply(lambda x: int(str(x).split(":")[0]))
        df['y'] = df['key'].apply(lambda x: int(str(x).split(":")[1]))
        df['elevation'] = self.meltMap(self.grid_elevation)['value']
        df['terrain'] = df['elevation'].apply(lambda x: self.landTypes(x))
        self.df_features = df
        
    #  Adding towns and to features map
    def add_features(self,features):
        """
        all features require both a key and a name in order to be placed on the map
        at this time only one feature per location is allowed
        existing feature is autmatcially overwritten
        """
        df = self.df_features
        for f in features:
            df.loc[f.key,'feature'] = f.name
            df.loc[f.key,'terrain'] = f.type

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
    def add_mountain(self,mdf):
        # mdf == a df of a mountain
        self.grid_elevation = self.grid_elevation.add(mdf.reindex_like(self.grid_elevation).fillna(0))

