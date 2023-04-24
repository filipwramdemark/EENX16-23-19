# predict
import numpy as np
import pandas as pd
from tensorflow import keras

def predict(X):

    model = keras.models.load_model('algoritm/NN/NN_model')

    label_to_wax_df = pd.read_csv('algoritm/label_to_wax.csv', names=['Label', 'Wax'])

    X = np.array([X])
    y = model.predict(X)
    ind = y[0].argsort()[-3:][::-1]


    wax = []
    for i in ind:
        wax.append(label_to_wax_df.at[i, 'Wax'])

    return wax