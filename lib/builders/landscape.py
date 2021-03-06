
default_params = {'grid':[40,40],
                'N_loc':0,
                'N_std':1,
                'water_level':20}

class Landscape:
    """
    the lanscape object takes a params file (generated by the webform), however there are defaults for everything and a global
    default_params if none is provided. This makes it easty to play with the parameters in a notebook.  
    """
    def __init__(self, params=default_params):
        #overal size of the world
        self.grid = params.get('grid',[40,40]) 
        #determinte the number and spread of mountain ranges
        self.drop_iter = params.get('drop_iter',5)
        self.spread_iter = params.get('spread_iter',80)
        self.mt_avg = params.get('mt_avg',2)
        self.mt_std = params.get('mt_std',3)
        self.peak_height = params.get('peak_height',5)
        self.mountain_level = params.get('mountain_level',25)
        #oceans
        self.water_level = params.get('water_level',5)
        self.rain_iter = params.get('rain_iter',8)
        self.rain_spread = params.get('rain_spread',100)
        #forests and deserts
        self.desert_threshold = params.get('desert_threshold',2)
        self.forest_threshold = params.get('forest_threshold',25)
        #other params that aren't used as variables
        self.N_loc = params.get('N_loc',0)
        self.N_std = params.get('N_std',1)
        # static things that don't ever change, regardless of format. 
        # Land types must exist as it is a global that is referenced in other places. 
        self.land_types = ['mountain','plain','desert','forest']
        self.terrain_types = ['ocean','mountain','plain','desert','forest']
        # Static landscape items:
        self.seasons = {
            0:'summer',
            1:'autumn',
            2:'winter',
            3:'spring'
        }
