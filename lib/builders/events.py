import pandas as pd
import numpy as np

class Events():
    def __init__(self,paths=None):
        if paths == "notebooks":
            self.events_df = pd.read_csv('../lib/Datasets/events.csv',index_col=0)
        else:
            self.events_df = pd.read_csv('game/lib/Datasets/events.csv',index_col=0)

def event_results(e,events,world,nations):
    choice = np.random.choice(events.index)
    event = events.loc[choice]
    #QA step, if the event calls for more subjects than there are nations
    n_sub = event.n_subjects
    if n_sub > len(world.nations):
        n_sub = len(world.nations)
    n_obj = event.n_objects
    if n_obj > len(world.nations):
        n_obj = len(world.nations)
    a = np.random.choice(world.nations,n_sub,replace=False).tolist()
    o = np.random.choice(world.nations,n_obj,replace=False).tolist()
    #the actuall affect of the event is done here. the event_var determines what the event actually affects.
    if event.effect_var == 'favor':
        nations.alter_favor(a,o,float(event.effect))
    text = (str(e) + ': ' +event.event.replace('{o}',str(o)).replace('{a}',str(a))) 
    return text

#now to run through the eons and let fate happen
def pass_through_time(world,events,nations):
    all_events = []
    for e in range(world.culture.eons):
        if np.random.random_sample()<world.culture.chaos:
            all_events.append(event_results(e,events,world,nations))
        else:
            all_events.append(f'{e}: nothing happend during this period.')
    return all_events

def add_chaos_to_world(world):
    world.df_features['danger'] = (world.df_features['key']
                                   .apply(lambda x: np.round(np.random.normal(world.culture.chaos, .3),3))
                                    )
    return world