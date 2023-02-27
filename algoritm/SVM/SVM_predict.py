import pandas as pd
import pickle


def predict(X):
    model = pickle.load(open('algoritm/SVM/SVM_model/svm_model.sav', 'rb'))

    label_to_wax_df = pd.read_csv('algoritm/label_to_wax.csv', names=['Label', 'Wax'])
    
    y = model.predict_proba([X])
    ind = y[0].argsort()[-3:][::-1]

    wax = []
    for i in ind:
        wax.append(label_to_wax_df.at[i, 'Wax'])

    return wax
