from matplotlib import pyplot as plt
from joblib import dump, load
from sklearn.tree import DecisionTreeClassifier 
from sklearn import tree
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as pl
import graphviz

data = pd.read_csv('algoritm/Valladata_prep.csv')
data = data.dropna(axis='columns')   
train, test = train_test_split(data, test_size = 0.2, shuffle = True) #splitting the data into training data
X = train.drop(columns='Valla (Label)')
y = train['Valla (Label)']

model = DecisionTreeClassifier(criterion = 'gini', random_state = 100)
model = model.fit(X, y)

# # text_representation = tree.export_text(model)
# # print(text_representation)


plt.figure(figsize=(30,10), facecolor ='k')
#create the tree plot
a = tree.plot_tree(model,
                   feature_names = X.columns,
                   #use the class names stored
                   class_names ='Valla (Label)' ,
                   rounded = True,
                   filled = True,
                   fontsize=14)
#show the plot
plt.show()

# dump(model, 'algoritm/Decision_Tree.joblib')
print(metrics.classification_report(test.drop(columns='Valla (Label)'),
                                    test['Valla (Label)']))


