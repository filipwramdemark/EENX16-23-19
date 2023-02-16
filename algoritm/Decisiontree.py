import numpy as np
import copy
import random
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.utils import resample

df = pd.read_excel(r'algoritm\Valladata.xlsx')
print(df)

# df = pd.read_excel(r'Valladata.xslx')
# print(df)
