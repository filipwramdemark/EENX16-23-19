import pandas as pd
import pickle
from Decisiontree import TreeNode



data =  {'Snötyp:': [0], 'Snötemperatur:': [0]}
testdata = pd.DataFrame.from_dict(data)
# print(testdata)
def Treepredict(data):
    model = pickle.load(open('algoritm/DecisionTree/Decision_Tree.pickle', "rb"))
    label_to_wax_df = pd.read_csv('algoritm/label_to_wax.csv', names=['Label', 'Wax'])    
    guessedlabel = model.predict(data.iloc[0])
    guess =(label_to_wax_df.at[guessedlabel, 'Wax'])
    return(guess)
print(Treepredict(testdata))
