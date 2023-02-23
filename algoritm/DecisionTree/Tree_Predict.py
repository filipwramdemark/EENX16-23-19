from joblib import load, dump
import pandas as pd
import pickle
from matplotlib import pyplot as plt
# from sklearn import tree
# import sys
# sys.path.insert(0,"C:\Users\kwaid\OneDrive\Dokument\Repo\Valla\EENX16-23-19\algoritm\DecisionTree")
# from DecisionTree import TreeNode
# from Decisiontree import TreeNode

# model = load('algoritm/DecisionTree/Decision_Tree.joblib')
model = pickle.load(open('algoritm/DecisionTree/Decision_Tree.pickle', "rb"))
label_to_wax_df = pd.read_csv('algoritm/label_to_wax.csv', names=['Label', 'Wax'])

data =  {'Snötyp:': [0], 'Snötemperatur:': [0]}
testdata = pd.DataFrame.from_dict(data)
# print(testdata)

guessedlabel = model.predict(testdata.iloc[0])
guess =(label_to_wax_df.at[guessedlabel, 'Wax'])
print(guess)
# print(tree.export_text(model))s

# plt.figure(figsize=(30,10), facecolor ='k')
# #create the tree plot
# a = tree.plot_tree(
#                    feature_names = testdata.columns,
#                    #use the class names stored
#                    class_names ='Valla (Label)' ,
#                    rounded = True,
#                    filled = True,
#                    fontsize=14)
#show the plot
# plt.show()