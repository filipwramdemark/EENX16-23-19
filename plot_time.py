import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('test.csv', header=None).values.tolist()

x_acc = []
y_acc = []
z_acc = []
t_x = []
t_y = []
t_z = []

t0 = data[0][1]

for i in range(len(data)):
    if abs(data[i][0]) < 100000:
        if i % 3 == 0:
            x_acc.append(data[i][0])
            t_x.append(data[i][1] - t0)
        elif i % 3 == 1:
            y_acc.append(data[i][0])
            t_y.append(data[i][1] - t0)
        else: 
            z_acc.append(data[i][0])
            t_z.append(data[i][1] - t0)

plt.figure("x_acc")
plt.xlabel("Tid (s)")
plt.ylabel("Acceleration (g m/s^2)")
plt.plot(t_x, x_acc)

plt.figure("z_acc")
plt.xlabel("Tid (s)")
plt.ylabel("Acceleration (g m/s^2)")
plt.plot(t_y, y_acc)

plt.show()