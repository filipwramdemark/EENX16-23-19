# predict
import numpy as np
import pandas as pd
from tensorflow import keras
from data_prep import label_to_wax

model = keras.models.load_model('algoritm/NN_model')

def predict(X):
    X = np.array([X])
    y = model.predict(X)
    ind = y[0].argsort()[-3:][::-1]


    wax = []
    for i in ind:
        wax.append(label_to_wax[i])

    return wax

print(predict([0,-5]))
