import pandas as pd

data = [0,1, 1]

def savefeedback(da):
    feedback =  {'Snötyp:': [da[0]], 'Snötemperatur:': [da[1]], 'Valla (Label)': [da[2]]}
    data = pd.DataFrame.from_dict(feedback)
    old = pd.read_csv('algoritm/Valladata_prep.csv')
    frames = [old,data]
    testdata =  pd.concat(frames)
    datatoexcel = pd.ExcelWriter('algoritm/Feedback.xlsx')
    testdata.to_excel(datatoexcel)
    datatoexcel.save()
    print('complete')
    return

savefeedback(data)
old = pd.read_csv('algoritm/Valladata_prep.csv')

old = old.head(5)
print('gamla')
print(old)
data = pd.read_excel('algoritm/Feedback.xlsx')
print('nya')
print(data)
frames = [old,data]
test =  pd.concat(frames)
test = test.drop('Unnamed: 0', axis=1)
print('Final')
print(test)