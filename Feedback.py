import pandas as pd

data = [0,1, 2]

def savefeedback(da):
    feedback =  {'Snötyp:': [da[0]], 'Snötemperatur:': [da[1]], 'Valla (Label)': [da[2]]}
    testdata = pd.DataFrame.from_dict(feedback)
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

print('Final')
print(test)