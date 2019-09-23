import numpy as np
import pandas as pd

def check_for_monsters(world):
    danger = world.df_features.loc[world.Character.get_location_key()].danger
    #return np.random.rand() < danger
    return True

def add_monsters_to_context(world,context):
    newcontext = context.copy()
    monsters = context['terrData']['monsters']
    allMonsters = [[m for i in range(np.random.randint(m['group_min'],m['group_max']))]
                    for m in monsters]
    newcontext['terrData']['monsters'] = allMonsters
    return newcontext


def makeMonsterDict(m):
    nameLetters = 'abcdefghijklmnopqrstuvwxyz'
    l = 6
    name = "".join([np.choose(nameLetters) for i in range(l)])
    m['id'] = name
    return m

class Monster:
    def __init__(m):
        self.name = "foo"
