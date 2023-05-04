import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('tests/test2/test33.csv', header=None).values.tolist()

x_acc = []
y_acc = []
z_acc = []
t_x = []
t_y = []
t_z = []

t0 = data[0][1]

for i in range(len(data)):
    if abs(data[i][0]) < 100000:
        if i % 2 == 0:
            x_acc.append(data[i][0])
            t_x.append(data[i][1] - t0)
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
plt.plot(t_z, z_acc)

plt.show()