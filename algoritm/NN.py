import numpy as np
import pandas as pd
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from sklearn.model_selection import train_test_split

# read the data
data = pd.read_excel('algoritm/Valladata.xlsx')

data = data.dropna(axis='columns')

# split into training and test set
train, test = train_test_split(data, test_size = 0.2, shuffle = True)

train_labels = train['Valla (Label)']
train_features = train.drop(columns = 'Valla (Label)')
test_labels = test['Valla (Label)']
test_features = test.drop(columns = 'Valla (Label)')

print(train_features)

#
num_classes = len(pd.Series(data['Valla (Label)']).unique())
batch_size = 32
epochs = 10

# preprocessing
y_train = keras.utils.np_utils.to_categorical(train_labels, num_classes)
y_test = keras.utils.np_utils.to_categorical(test_labels, num_classes)


# define the model
model = Sequential()
model.add(Dense(64, activation = 'relu'))
model.add(Dense(64, activation = 'relu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(
    loss=keras.losses.categorical_crossentropy,
    optimizer=tf.keras.optimizers.SGD(learning_rate = 0.1),
    metrics=['accuracy'],)

# train the model
fit_info = model.fit(train_features, train_labels,
           batch_size=batch_size,
           epochs=epochs,
           verbose=1,
           validation_data=(test_features, test_labels))
score = model.evaluate(test_features, test_labels, verbose=0)
print('Test loss: {}, Test accuracy {}'.format(score[0], score[1]))
