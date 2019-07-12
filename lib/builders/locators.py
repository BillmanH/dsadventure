import numpy as np
import pandas as pd

def keyChord(key):
    '''
    takes a key "1,1", returns a coord [1,1]
    '''
    coord = key.split(":")
    return [int(coord[0]),int(coord[1])]