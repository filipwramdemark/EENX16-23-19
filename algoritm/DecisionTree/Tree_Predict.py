from joblib import load, dump
import pandas as pd
import pickle


model = load('algoritm/DecisionTree/Decision_Tree.joblib')
# model = pickle.load(open('algoritm/DecisionTree/Decision_Tree.pickle', "rb"))
label_to_wax_df = pd.read_csv('algoritm/label_to_wax.csv', names=['Label', 'Wax'])

data =  {'Snötyp:': [0], 'Snötemperatur:': [0]}
testdata = pd.DataFrame.from_dict(data)
# print(testdata)

guessedlabel = model.predict(testdata.iloc[0])
guess =(label_to_wax_df.at[guessedlabel, 'Wax'])
print(guess)
