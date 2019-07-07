import numpy as np
import pandas as pd

def keyChord(key):
    '''
    takes a key "1,1", returns a coord [1,1]
    '''
    coord = key.split(":")
    return [int(coord[0]),int(coord[1])]

#TODO: Namegen has bug that can't convert blank values to str. Change to import as STR not NaN.
nameparts = pd.read_csv('../lib/Datasets/namegen.csv')

class Landscape
