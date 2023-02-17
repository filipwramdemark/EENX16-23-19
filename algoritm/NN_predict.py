# predict
import numpy as np
from tensorflow import keras
# from NN import label_to_wax

model = keras.models.load_model('algoritm/NN_model')

# wax = label_to_wax[np.argmax(y)]

def predict(X):
    X = np.array([X])
    y = model.predict(X)
    ind = np.argpartition(y[0], -3)[-3:]
    print(y)
    return ind

print(predict([0,0]))