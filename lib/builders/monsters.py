import numpy as np
import pandas as pd

def check_for_monsters(world):
    danger = world.df_features.loc[world.Character.get_location_key()].danger
    return np.random.rand() < danger

def add_monsters_to_context(world,context):
    newcontext = context.copy()
    newcontext['monsters'] = []
    return newcontext
