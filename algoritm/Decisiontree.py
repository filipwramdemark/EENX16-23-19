import numpy as np
import copy
import random
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.utils import resample

df = pd.read_excel('Valladata.xslx')
print(df)