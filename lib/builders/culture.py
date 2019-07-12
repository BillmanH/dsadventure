default_params = {}

class Culture:
    """
    Culture are the parameters for everything that affects people, cities, nations and politics.
    """
    def __init__(self, params=default_params):
        #the number of nations
        self.n_nations = params.get('n_nations',8)
        #overal age of the 'civilized era' (age of unconflicted growth)
        self.eons = params.get('eons',10)
        #the number of towns spawned per iteration
        self.town_spawn = params.get('town_spawn',1)
        #the likelyhood a town will increase in size
        self.town_birthrate = params.get('town_birthrate',.3)