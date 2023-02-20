# predict
import numpy as np
import pandas as pd
from tensorflow import keras

model = keras.models.load_model('algoritm/NN_model')

label_to_wax_df = pd.read_csv('algoritm/label_to_wax.csv', names=['Label', 'Wax'])
label_to_wax = label_to_wax_df.set_index('Label').T.to_dict('list')

def predict(X):
    X = np.array([X])
    y = model.predict(X)
    ind = y[0].argsort()[-3:][::-1]


    wax = []
    for i in ind:
        wax.append(label_to_wax[i][0])

    return wax

print(predict([0,-5]))
