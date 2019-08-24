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
    return world

#the second age (and after) require a world object and modify it
def the_second_age(world,default_params,c=c):
    world.culture = c.Culture(params=default_params)
    all_towns = towns.build_towns(world,people)
    world.add_features(all_towns)
    world.towns = all_towns
    all_nations,k = nations.cluster_nations(world)
    world.nations = all_nations                  
    world.df_features = nations.predict_nations(k,world)
    #set town's starting loyalty to it's nation
    for t in all_towns:
        try:
            t.set_starting_fielty(world)
        except:
            continue
    for n in np.unique(world.df_features['nation'].dropna()):
        #TODO: having an error where sometimes a nation contains no cities
        try:
            c = world.df_features[(world.df_features['nation']==n)& \
                (world.df_features['terrain']=='town')]['feature'].tolist()
            #getting the town objects
            ts = [ti for ti in all_towns if ti.name in c]
            #get population(p)
            p = [tii.pop for tii in ts]
            #getting the first town that has the max population, make that the capitol
            ts[np.argmax(p)].type='capitol'
        except:
            continue
    world.nations = [nations.Nation(n,world,world.culture,people) for n in world.nations.values()]
    world.towns = all_towns
    return world

#params for culture and world should be set. the only thing here is to unravle the events that create the people, buildings and adventure.
def the_third_age(world):
    path = os.listdir()
    e = events.Events()
    all_events = events.pass_through_time(world,e.events_df,nations)
    return world,all_events


