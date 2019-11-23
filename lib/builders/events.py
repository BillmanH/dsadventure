import pandas as pd
import numpy as np

from game.models import events
from game.lib.builders import nations

def get_possible_events():
    return [str(i[0]) for i in events.objects.values_list('key')]

def get_event(k,paths='prod'):
    m = events.objects.get(pk=k)
    return m

class Events():
    def __init__(self,paths=None):
        if paths == "notebooks":
            self.events_df = pd.read_csv('../lib/Datasets/events.csv',index_col=0)
        else:
            self.events_df = pd.read_csv('game/lib/Datasets/events.csv',index_col=0)

def str_munge(x,a,o,t):
        return (x.replace('{o}',str(o))
                .replace('{a}',str(a))
                .replace('{t}',str(t))
                ) 

def give_message(world,event,a,o,t):
    """
    where
        message - the text string to be delivered
        a - the nation that is the subject (originator) of the event
        o - the nation that is the object (reciever) of the event
    """
    for i in a:
        for town in i.towns:
            [p.add_message(str_munge(event.a_message, a,o,t)) for p in town.population]
    for i in o:
        for town in i.towns:
            [p.add_message(str_munge(event.a_message, a,o,t)) for p in town.population]
        

def event_results(e,world):
    choice = np.random.choice(get_possible_events())
    event = get_event(choice)
    #QA step, if the event calls for more subjects than there are nations
    n_sub = event.n_subjects
    if n_sub > len(world.nations):
        n_sub = len(world.nations)
    n_obj = event.n_objects
    if n_obj > len(world.nations):
        n_obj = len(world.nations)
    if n_obj+n_sub > len(world.nations):
        n_obj = 1
    a = np.random.choice(world.nations,n_sub,replace=False).tolist()
    o = np.random.choice(world.nations,n_obj,replace=False).tolist()
    #the actuall affect of the event is done here. the event_var determines what the event actually affects.
    if event.effect_var == 'favor':
        nations.alter_favor(a,o,float(event.effect))
        t=''
    if event.effect_var == 'feature':
        t = nations.place_feature(world,a,o,event)
    if event.effect_var == 'buildings':
        t = nations.place_building(a,o,event)
    text = str(e) + ': ' + str_munge(event.event,a,o,t)
    give_message(world,event,a,o,t)
    return text

#now to run through the eons and let fate happen
def pass_through_time(world,events):
    all_events = []
    for e in range(world.culture.eons):
        if np.random.random_sample()<world.culture.chaos:
            all_events.append(event_results(e,world))
        else:
            all_events.append(f'{e}: nothing happend during this period.')
    return all_events

def add_chaos_to_world(world):
    world.df_features['danger'] = (world.df_features['key']
                                   .apply(lambda x: np.round(np.random.normal(world.culture.chaos, .3),3))
                                    )
    return world


    
