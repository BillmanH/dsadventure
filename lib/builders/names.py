import numpy as np
import pandas as pd

#TODO: Namegen has bug that can't convert blank values to str. Change to import as STR not NaN.
nameparts = pd.read_csv('../lib/Datasets/namegen.csv')

prefixes = pd.read_excel('../lib/Datasets/townNames.xlsx',sheet_name='prefix')['Settlement name (part 1)'].tolist()
suffixes = pd.read_excel('../lib/Datasets/townNames.xlsx',sheet_name='suffix')['Settlement name (part 2)'].tolist()

