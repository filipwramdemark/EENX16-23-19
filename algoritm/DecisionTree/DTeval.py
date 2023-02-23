import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle
from joblib import load, dump
import graphics as gp
from Decisiontree import Classification_eval
tree = pickle.load(open('algoritm/DecisionTree/Decision_Tree.pickle', "rb"))
data = pd.read_csv('algoritm/Valladata_prep.csv')
data = data.dropna(axis='columns')   
train, test = train_test_split(data, test_size = 0.2, shuffle = True)


def eval():
    y = test['Valla (Label)']
    x = test.drop(columns='Valla (Label)')
    log = Classification_eval()

    for i in range(x.shape[0]):
        pred = tree.predict(x.iloc[i])
        log.update(pred, y.iloc[i])
            
    print('accuarcy', log.accuracy())
    print('precision', log.precision())
    print('recall', log.recall())


eval()
win = gp.GraphWin("My Window", 1800, 950)
tree.print_childs(win, 1800, 900,'l', 0, 0)
print(tree.countnodes())
input('wait')
win.close()
pickle.dump(tree, open('algoritm/DecisionTree/Decision_Tree.pickle', "wb"))
# clf = load('algoritm/Decision_Tree2.joblib')
# print(tree.print_childs())
data =  {'Snötyp:': [0], 'Snötemperatur:': [1]}
testdata = pd.DataFrame.from_dict(data)
guessedlabel = tree.predict(testdata.iloc[0])
# dump(tree, 'algoritm/Decision_Tree.joblib')
# print(tree.child_nodes)
# tree.print_childs