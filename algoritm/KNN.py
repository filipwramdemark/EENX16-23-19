import pandas as pd
import matplotlib.pyplot as plt
import numpy
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.metrics import confusion_matrix  


import math


#Dataset with valla imported 
#data = pd.read_excel(r'algoritm/Valladata.xlsx')
data = pd.read_csv(r'algoritm/Valladata_prep.csv')
print(data)

#Data being loaded, executed
#snötyp samt vallatypen 
x = data.iloc[:, 0: 2].values
print(x)

#vallatyper (lable) 
y = data.iloc[:,2].values
print(y)

#print(data.shape)

#Data being split into training and test
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.25, random_state=0)  
print(x_test)
print(y_test)
#print(y_test.shape)
#print(x_test.shape)


#jsksks
st_x= StandardScaler()    
x_train= st_x.fit_transform(x_train)    
x_test= st_x.transform(x_test)



#Running the classifier
KNN = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)  
KNN.fit(x_train, y_train)
#metric='minkowski'
print(KNN)

#predicting 
predict_y = KNN.predict(x_test)
print(predict_y)

print("Accuracy:",metrics.accuracy_score(y_test, predict_y))

confusion_matrix= metrics.confusion_matrix(y_test, predict_y)  

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])

cm_display.plot()
plt.show()
print('Accuracy:', metrics.accuracy_score(y_test, predict_y))



#snowtemp = list(data['Snötemperatur:'])
#print(snowtemp)
#snowtype = list(data['Snötyp:'])
#print(snowtype)

#A = data.iloc[0:,0:3]
#print(A)

#lables = data.labels_

##residue_name = list(data.index)
#print(residue_name)

#print('hello')