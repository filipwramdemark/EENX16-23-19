from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay)
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt
paths = []
# for i in range(1, 37):
#     paths.append(f'tests/test2/test{i}.csv')
# print(paths)

df = []
david = [1,2,3,7,8,9,13,14,15,19,20,21,25,26,27,31,31,33]
nora = [4,5,6,10,11,12,16,17,18,22,23,24,28,29,30,34,35,36]
# for idx in range(1, 37):
for idx in nora:
    if idx <=18:
        label =True
    else: 
        label = False
    z_acc=[]
    x_acc=[]

    x_delta = []
    z_delta = []
    data = pd.read_csv(f'tests/test2/test{idx}.csv').values.tolist()
    for i in range(len(data)):
        if abs(data[i][0]) < 100000:
            if i % 2 == 0:
                x_acc.append(data[i][0])
            
            else: 
                z_acc.append(data[i][0])
    for a in range(len(x_acc)-1):
        if x_acc[a] > 3.5:
        
        
            if len(df) > 0:
            # data= {'x_acc': [x_acc], 'z_acc': [z_acc], 'Label': [label]}
                tempdf = pd.DataFrame([label]+x_acc[a-25:a+25]).T
                frames = [df,tempdf]
                df = pd.concat(frames)
            else:
            # data = {'x_acc': [x_acc], 'z_acc': [z_acc], 'Label': [label]}
                df = pd.DataFrame([label]+x_acc[a-25:a+25]).T

            # x_delta.append(x_acc[a+1]-x_acc[a])
            # z_delta.append(z_acc[a+1]-z_acc[a])




# print(df.head())

df.to_csv("SVC_test.csv", index=False, header=False)

print('skoj')
df.fillna(0, inplace=True)
print('fillna complete')
y =  df.iloc[:, 0]
X = df.iloc[:,1:].to_numpy()
print('Börja spliten')
# X =np.nan_to_num(X)

train_X, test_X , train_y, test_y = train_test_split(X,y,test_size=0.2,shuffle=True)
print(train_y)
# print(train_X)

# train_y = train_y.label.values
# train_X = train_X.to_numpy()


# print(train_X)

print('SVC starta')
model = SVC(C=1, kernel='rbf', decision_function_shape='ovr', probability=True)
print('SVC tränar')
model.fit(train_X, train_y)
print('Svc tränad')
pred_labels = model.predict(test_X)

acc = accuracy_score(test_y, pred_labels)
print(test_y)
print(pred_labels)
print(acc)

Multi_cm = confusion_matrix(test_y,pred_labels)
disp = ConfusionMatrixDisplay(confusion_matrix=Multi_cm, display_labels=['Bra valla', 'Dålig valla']) #Målar upp matrixen
fig, ax = plt.subplots(figsize=(3, 3))
disp.plot(ax=ax)
plt.show()
# data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}

# data = pd.read_csv('tests/test2/test1.csv').values.tolist()



   
# data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
# pd.DataFrame.from_dict(data)
