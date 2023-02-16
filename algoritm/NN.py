import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split

# read the data
data = pd.read_excel('algoritm/Valladata.xlsx')

# split into training and test set
train, test = train_test_split(data, test_size = 0.2, shuffle = True)

train_labels = train['Valla (Label)']
train_features = train.drop(columns = 'Valla (Label)')
test_labels = test['Valla (Label)']
test_features = test.drop(columns = 'Valla (Label)')


