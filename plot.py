import matplotlib.pyplot as plt
import pandas as pd
import scipy.integrate as it
import statistics

acc = pd.read_csv('acc_test1.csv', header=None).values.tolist()

x_acc = []
y_acc = []
z_acc = []

for i in range(len(acc)):
    if abs(acc[i][0]) < 100000:
        if i % 3 == 0:
            x_acc.append(acc[i][0])
        elif i % 3 == 1:
            y_acc.append(acc[i][0])
        else: 
            z_acc.append(acc[i][0])

plt.figure("x_acc")
plt.title("x acceleration")
plt.plot(x_acc)

plt.figure("y_acc")
plt.title("y acceleration")
plt.plot(y_acc)

plt.figure("z_acc")
plt.title("z acceleration")
plt.plot(z_acc)

plt.show()