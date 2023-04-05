import pandas as pd

acc = pd.read_csv('acc_test2.csv', header=None).values.tolist()

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

def slip_count():
    max_acc = max(x_acc)
    i = 0
    high_ind = []
    while i < len(x_acc):
        if x_acc[i] > 0.6 * max_acc:
            high_ind.append(i)
            while (i < len(x_acc) - 1) and (x_acc[i+1] >  0.6 * max_acc):
                i += 1
        i += 1
    f = (high_ind[-1] - high_ind[0]) / len(high_ind)

    slip_counter = 0
    for i in range(len(high_ind)-1):
        if (high_ind[i+1] - high_ind[i] < f / 2):
            slip_counter += 1

    return slip_counter
