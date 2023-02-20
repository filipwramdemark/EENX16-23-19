import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
import math



#data = pd.read_excel(r'algoritm/Valladata.xlsx')
data = pd.read_csv(r'algoritm/Valladata_prep.csv')
print(data)

#snowtemp = list(data['Snötemperatur:'])
#print(snowtemp)
#snowtype = list(data['Snötyp:'])
#print(snowtype)

#A = data.iloc[0:,0:3]
#print(A)

#lables = data.labels_

##residue_name = list(data.index)
#print(residue_name)

#print('hello')