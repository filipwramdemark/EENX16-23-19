from joblib import load
import pandas as pd

tree = load('algoritm/Decision_Tree.joblib')
label_to_wax_df = pd.read_csv('algoritm/label_to_wax.csv', names=['Label', 'Wax'])

data =  {'Snötyp:': [0], 'Snötemperatur:': [1]}
testdata = pd.DataFrame.from_dict(data)
# print(testdata)

guessedlabel = tree.predict(testdata.iloc[0])
guess =(label_to_wax_df.at[guessedlabel, 'Wax'])
print(guess)