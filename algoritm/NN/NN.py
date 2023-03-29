import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from sklearn.model_selection import train_test_split

# read the data
data = pd.read_csv('algoritm/Valladatamer_prep.csv')
data = data.dropna(axis='columns')

# split into training and test set
train, test = train_test_split(data, test_size = 0.2, shuffle = True)

train_labels = train['Valla (Label)']
train_features = train.drop(columns = 'Valla (Label)')
test_labels = test['Valla (Label)']
test_features = test.drop(columns = 'Valla (Label)')

# normalize the data
for df in [train_features, test_features]:
    for col in train_features.columns:
        df[col] = df[col] / df[col].abs().max()

    df['Snötyp:'] = df['Snötyp:'] * 10

print(train_features)

train_features = np.asarray(train_features).astype(np.float32)
test_features = np.asarray(test_features).astype(np.float32)

train_labels = np.asarray(train_labels).astype(np.float32)
test_labels = np.asarray(test_labels).astype(np.float32)

# parameters
num_classes = len(pd.Series(data['Valla (Label)']).unique())
batch_size = 8
epochs = 20

# define the model
model = Sequential()
model.add(Dense(64, activation = 'relu', input_shape=(2,)))
model.add(Dense(32, activation = 'relu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(
    loss = tf.keras.losses.SparseCategoricalCrossentropy(),
    optimizer = tf.keras.optimizers.SGD(learning_rate = 0.3),
    metrics = ['accuracy'])

# train the model
fit_info = model.fit(train_features, train_labels,
           batch_size = batch_size,
           epochs = epochs,
           verbose = 1,
           validation_data = (test_features, test_labels))

score = model.evaluate(test_features, test_labels, verbose=0)

print('Test loss: {}, Test accuracy {}'.format(score[0], score[1]))

model.save('algoritm/NN/NN_model')
