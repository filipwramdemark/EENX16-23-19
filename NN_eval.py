import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from sklearn.model_selection import train_test_split

df = pd.DataFrame()

for i in range(1,37):
    if i <= 18:
        label =True
    else: 
        label = False

    z_acc=[]
    x_acc=[]

    data = pd.read_csv(f'tests/test2/test{i}.csv').values.tolist()
    for i in range(len(data)):
        if abs(data[i][0]) < 100000 and i < 2600:
            if i % 2 == 0:
                x_acc.append(data[i][0])
            else: 
                z_acc.append(data[i][0])

    testdf = pd.DataFrame([label]+x_acc+z_acc).T
    df = pd.concat([df,testdf])



# split into training and test set
train, test = train_test_split(df, test_size = 0.2, shuffle = True)

train_labels = train.iloc[:,0]
train_features = train.iloc[:,1:]
test_labels = test.iloc[:,0]
test_features = test.iloc[:,1:]

# normalize the data
for df in [train_features, test_features]:
    for col in train_features.columns:
        df[col] = df[col] / df[col].abs().max()


train_features = np.asarray(train_features).astype(np.float32)
test_features = np.asarray(test_features).astype(np.float32)

train_labels = np.asarray(train_labels).astype(np.float32)
test_labels = np.asarray(test_labels).astype(np.float32)

print(train_labels)


# parameters
num_classes = 2
batch_size = 8
epochs = 20

# define the model
model = Sequential()
model.add(Dense(128, activation = 'relu'))
model.add(Dense(256, activation = 'relu'))
model.add(Dense(128, activation = 'relu'))
model.add(Dense(64, activation = 'relu'))
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
