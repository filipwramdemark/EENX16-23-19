import matplotlib.pyplot as plt
import pandas as pd

acc = pd.read_csv('tests/test1/acc_test1.csv', header=None).values.tolist()

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
x_vel = [0] * len(x_acc)            
for i in range(len(x_acc)): 
    if x_acc[i] <0.1 and x_acc[i] >-0.1:
        x_acc[i] = 0
for a in range(len(x_acc)):
    if a == 0:
        x_vel[a] = x_acc[a]
    else: 
        x_vel[a] = x_acc[a] + x_vel[a-1]
    


plt.figure("x_acc")
plt.xlabel("Datapunkt")
plt.ylabel("Acceleration (g m/s^2)")
plt.plot(x_acc)

plt.figure("x_vel")
plt.xlabel("Datapunkt")
plt.ylabel("Acceleration (g m/s^2)")
plt.plot(x_vel)

# plt.figure("z_acc")
# plt.xlabel("Datapunkt")
# plt.ylabel("Acceleration (g m/s^2)")
# plt.plot(z_acc)

plt.show()