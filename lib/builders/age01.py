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

default_params = {'grid':[40,40],
                'N_loc':0,
                'N_std':1}

class Landscape:
    def __init__(self, params=default_params):
        #overal size of the world
        self.grid = params.get('grid',[40,40]) 
        #determinte the number and spread of mountain ranges
        self.drop_iter = params.get('drop_iter',5)
        #other params that aren't used as variables
        self.N_loc = params.get('N_loc',0)
        self.N_std = params.get('N_std',1)
        
class World:
    def __init__(self,landscape):
        self.landscape = landscape
        self.land_shifts = []

        self.grid_elevation = self.build_blank_grid(landscape) 

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
        nextcoord = np.add(coord,get_random_direction())
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

    def brownian_land(self,landscape):
        df_new = self.grid_elevation
        for n in range(landscape['drop_iter']):
            coord = get_random_chord(df_new)
            landscape['peaks'].append(coord)
            for m in range(landscape['spread_iter']):
                try:
                    coord = get_next_coord(coord)
                    m = getMountain(height=abs(
                                    int(np.round(
                                        np.random.normal(landscape['mt_avg'], landscape['mt_std']))
                                      )))
                   mdf = reindexMountain(coord,m)
                    df_new = df_new.add(mdf.reindex_like(df_new).fillna(0))
                except:
                    continue
        return df_new

    # the world starts here with a blank canvas
    def build_blank_grid(self,landscape):
        return pd.DataFrame(columns=range(landscape.grid[1]),index=range(landscape.grid[0])).fillna(0)

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

