import pandas as pd
import numpy as np
import pickle
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
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

train_features = np.asarray(train_features).astype(np.float32)
test_features = np.asarray(test_features).astype(np.float32)

train_labels = np.asarray(train_labels).astype(np.float32)
test_labels = np.asarray(test_labels).astype(np.float32)

# define and train the model
model = SVC(C=1, kernel='rbf', decision_function_shape='ovr', probability=True)
model.fit(train_features, train_labels)

# save the model
pickle.dump(model, open('algoritm/SVM/SVM_model/svm_model.sav', 'wb'))

# evaluate the model
pred_labels = model.predict(test_features)

acc = accuracy_score(test_labels, pred_labels)

print('Accuracy:', acc)