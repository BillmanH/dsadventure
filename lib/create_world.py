import pandas as pd
import numpy as np

from .builders import world as w, landscape as l

def the_first_age(default_params):
    landscape = l.Landscape(params=default_params)
    world = w.World(landscape)
    world.shift_terrain()
    world.brownian_land()
    world.brownian_rainfall()
    world.build_df_features()
    return world

