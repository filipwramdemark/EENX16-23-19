import numpy as np
import pandas as pd
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# read the data
data = pd.read_excel('algoritm/Valladata.xlsx')

data = data.dropna(axis='columns')

# d = {'Valla (Label)': [0,1,2,3,1,2,4,2,0,1], 'Temp': [10,9,8,-7,6,5,4,3,2,1]}
# data = pd.DataFrame(data=d)

snow_to_label = {}
label_to_snow = {}

wax_to_label = {}
label_to_wax = {}

for i in data.index:
    if data.at[i, 'Snötyp:'] not in snow_to_label:
        snow_to_label[data.at[i, 'Snötyp:']] = len(snow_to_label)
        label_to_snow[len(label_to_snow)] = data.at[i, 'Snötyp:']
    
    data.at[i, 'Snötyp:'] = snow_to_label[data.at[i, 'Snötyp:']]

    if data.at[i, 'Valla (Label)'] not in wax_to_label:
        wax_to_label[data.at[i, 'Valla (Label)']] = len(wax_to_label)
        label_to_wax[len(label_to_wax)] = data.at[i, 'Valla (Label)']
    
    data.at[i, 'Valla (Label)'] = wax_to_label[data.at[i, 'Valla (Label)']]



# split into training and test set
train, test = train_test_split(data, test_size = 0.2, shuffle = True)

train_labels = train['Valla (Label)']
train_features = train.drop(columns = 'Valla (Label)')
test_labels = test['Valla (Label)']
test_features = test.drop(columns = 'Valla (Label)')

train_features = np.asarray(train_features).astype(np.float32)
test_features = np.asarray(test_features).astype(np.float32)

train_labels = np.asarray(train_labels).astype(np.float32)
test_labels = np.asarray(test_labels).astype(np.float32)

# parameters
num_classes = len(pd.Series(data['Valla (Label)']).unique())
batch_size = 8
epochs = 20

# preprocessing


# define the model
model = Sequential()
model.add(Dense(64, input_shape=(2,), activation = 'relu'))
model.add(Dense(64, activation = 'relu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(
    loss = tf.keras.losses.SparseCategoricalCrossentropy(),
    optimizer = tf.keras.optimizers.SGD(learning_rate = 0.1),
    metrics = ['accuracy'])

# train the model
fit_info = model.fit(train_features, train_labels,
           batch_size = batch_size,
           epochs = epochs,
           verbose = 1,
           validation_data = (test_features, test_labels))

score = model.evaluate(test_features, test_labels, verbose=0)

print('Test loss: {}, Test accuracy {}'.format(score[0], score[1]))

# predict

X = np.array([[0,-5]])

y=model.predict(X)

wax = label_to_wax[np.argmax(y)]

print(wax)