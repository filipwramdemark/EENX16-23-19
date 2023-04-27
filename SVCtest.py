from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
paths = []
# for i in range(1, 37):
#     paths.append(f'tests/test2/test{i}.csv')
# print(paths)
z_acc=[]
x_acc=[]
df = []
for idx in range(1, 37):
    
    data = pd.read_csv(f'tests/test2/test{idx}.csv').values.tolist()
    for i in range(len(data)):
        if abs(data[i][0]) < 100000:
            if i % 2 == 0:
                x_acc.append(data[i][0])
            
            else: 
                z_acc.append(data[i][0])
    if idx <=19:
        label =True
    else: 
        label = False
    if len(df) > 0:
        # data= {'x_acc': [x_acc], 'z_acc': [z_acc], 'Label': [label]}
        tempdf = pd.DataFrame([label]+x_acc+z_acc)
        frames = [df,tempdf]
        df = pd.concat(frames)
    else:
        # data = {'x_acc': [x_acc], 'z_acc': [z_acc], 'Label': [label]}
        df = pd.DataFrame([label]+x_acc+z_acc).T
print(df.head())
# z_acc=[]
# x_acc=[]
# data_list = []
# for idx in range(1, 37):
#     data = pd.read_csv(f'tests/test2/test{idx}.csv').values.tolist()
#     for i in range(len(data)):
#         if abs(data[i][0]) < 100000:
#             if i % 2 == 0:
#                 x_acc.append(data[i][0])
            
#             else: 
#                 z_acc.append(data[i][0])
#     if idx <=19:
#         label =True
#     else: 
#         label = False
#     data_list.append({'x_acc': x_acc, 'z_acc': z_acc, 'Label': label})
    
# df = pd.DataFrame(data_list)    
# print(df)
y =  df.iloc[:, 0]
X = df.iloc[:,1:].to_numpy()


train_X, test_X , train_y, test_y = train_test_split(X,y,test_size=0.2,shuffle=True)

# train_y = train_y.label.values
train_X = train_X.to_numpy()


# print(train_X)

# print(train_X)
model = SVC(C=1, kernel='rbf', decision_function_shape='ovr', probability=True)
model.fit(train_X, train_y)

# pred_labels = model.predict(test_X)

# acc = accuracy_score(test_y, pred_labels)
# print(acc)
# data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}

# data = pd.read_csv('tests/test2/test1.csv').values.tolist()



   
# data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
# pd.DataFrame.from_dict(data)
