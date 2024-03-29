import pandas as pd
import pickle
from algoritm.DecisionTree.Decisiontree import *



# data =  {'Snötyp:': [0], 'Snötemperatur:': [0]}
# testdata = pd.DataFrame.from_dict(data)
# 
# test = [0,1]

def Treepredict(lista):
    data =  {'Snötyp:': [lista[0]], 'Snötemperatur:': [lista[1]], 'Fuktighet snö:': [lista[2]], 'Temperatur luft:': [lista[3]], 'Luftfuktighet:': [lista[4]]}
    testdata = pd.DataFrame.from_dict(data)
    model = pickle.load(open('algoritm/DecisionTree/Decision_Tree.sav', 'rb'))
    label_to_wax_df = pd.read_csv('algoritm/label_to_wax.csv', names=['Label', 'Wax'])    
    guessedlabel = model.predict(testdata.iloc[0])
    guess =(label_to_wax_df.at[guessedlabel, 'Wax'])
    return(guess)
# print(Treepredict(test))