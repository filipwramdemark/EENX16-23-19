import pandas as pd


#Tar in datan som en lista
def savefeedback(da):
    #Formaterar datan som vi vill ha den
    feedback =  {'Snötyp:': [da[0]], 'Snötemperatur:': [da[1]], 'Valla (Label)': [da[2]], 'Fuktighet snö:': [da[3]], 'Temperatur luft:' : [da[4]] , 'Luftfuktighet:': [da[5]]}
    #Gör om datan till en dataframe
    data = pd.DataFrame.from_dict(feedback)
    old = pd.read_csv('algoritm/Feedback.csv')
    frames = [old,data]
    #Kombinerar den nya och den gamla datan
    testdata =  pd.concat(frames)
    #Sparar datan
    testdata.to_csv('algoritm/Feedback.csv', index=False)
    print('complete')


