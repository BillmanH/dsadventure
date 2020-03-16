import pandas as pd
import numpy as np
import os

from .builders import world as w, landscape as l, culture as c
from .builders import people,towns,nations,events

#the first age creates the world object from scratch
def the_first_age(default_params):
    landscape = l.Landscape(params=default_params)
    world = w.World(landscape)
    world.shift_terrain()
    world.brownian_land()
    world.brownian_rainfall()
    world.build_df_features()
    #once df_features is created you can do more fine-tuned details.
    world.df_features['terrain'] = world.df_features.apply(lambda x: w.set_ecology(x,landscape),axis = 1)
    world.year = 1000
    return world

#the second age (and after) require a world object and modify it
def the_second_age(world, default_params, c=c):
    world.year += 100
    world.towns = []
    world.nations = []
    world.population = []
    world.culture = c.Culture(params=default_params)
    all_towns = towns.build_towns(world, people)
    world.add_features(all_towns)
    world.towns = all_towns
    k = nations.cluster_nations(world)
    [n.set_capitol(world) for n in world.nations]
    [nations.appoint_ruler(world, n, people) for n in world.nations]
    return world

#params for culture and world should be set. the only thing here is to unravle the events that create the people, buildings and adventure.
def the_third_age(world):
    path = os.listdir()
    e = events.get_possible_events()
    all_events = events.pass_through_time(world)
    world.df_features['visited'] = 0
    world.df_features['aware'] = 0
    world.df_features['turn_last_visited'] = 0
    world = events.add_chaos_to_world(world)
    return world,all_events


