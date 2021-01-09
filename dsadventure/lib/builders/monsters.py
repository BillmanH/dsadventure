import numpy as np
import pandas as pd

def check_for_monsters(world):
    danger = world.df_features.loc[world.Character.get_location_key()].danger
    #for dev purposes, set danger to one to make monsters always show up. 
    #danger = 1
    return np.random.rand() < danger

def add_monsters_to_context(world,context):
    newcontext = context.copy()
    monsters = context['terrData']['monsters']
    allMonsters=[]
    for m in monsters:
        listOfMonsters = []
        for i in range(np.random.randint(m['group_min'],m['group_max'])):
            mi = m.copy()
            #make random id for each creture
            nameLetters = list('abcdefghijklmnopqrstuvwxyz')
            mid = "".join(np.random.choice(nameLetters,6))
            mi['id'] = mid
            listOfMonsters.append(mi)
        allMonsters.append(listOfMonsters)

       #allMonsters = [[makeMonsterDict(m) for i in range(np.random.randint(m['group_min'],m['group_max']))]
       #             for m in monsters]
    newcontext['terrData']['monsters'] = allMonsters
    return newcontext


class Monster:
    def __init__(m):
        self.name = "foo"
