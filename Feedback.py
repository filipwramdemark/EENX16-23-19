import pandas as pd

data = [0,1, 2]

def savefeedback(da):
    feedback =  {'Snötyp:': [da[0]], 'Snötemperatur:': [da[1]]}
    testdata = pd.DataFrame.from_dict(feedback)
    datatoexcel = pd.ExcelWriter('algoritm/Feedback.xlsx')
    testdata.to_excel(datatoexcel)
    datatoexcel.save()
    print('complete')
    return

savefeedback(data)

data = pd.read_excel('algoritm/Feedback.xlsx')
print(data)

