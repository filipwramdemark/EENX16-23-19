import matplotlib.pyplot as plt
import pandas as pd
from statistics import mode
# data = pd.read_csv('tests/test1/acc_test1.csv', header=None).values.tolist()
data = pd.read_csv('tests/sim_case1/test3.csv', header=None).values.tolist()

x_acc = []
y_acc = []
z_acc = []
t_x = []
t_z = []
t_y = []
print(data[0])
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
x_vel = [0] * len(x_acc)
x_comp = []            
# for i in range(len(x_acc)): 
#     if x_acc[i] <0.1 and x_acc[i] >-0.1:
#         x_comp.append(x_acc[i])
# average = sum(x_comp) / len(x_comp)
# if average < 0:
#     new_comp = [x for x in x_comp if x<0]
# else: 
#     new_comp = [x for x in x_comp if x>0]
# new_average = sum(new_comp)/ len(new_comp)
# for idx in range(len(x_acc)):
#     x_acc[idx] = x_acc[idx] - new_average
acc_comp = []
for a in x_acc:
    if (a <0.1) and (a >-0.1):
        acc_comp.append(a)

# average = sum(acc_comp)/ len(acc_comp)
average = mode(acc_comp)
print(average)

for idx in range(len(x_acc)):
    x_acc[idx] = x_acc[idx]- average
    



for a in range(len(x_acc)):
    if a == 0:
        x_vel[a] = x_acc[a] * t_x[a]
    else: 
        x_vel[a] = (x_acc[a] * t_x[a] ) + x_vel[a-1]
# total_error = x_vel[-1]
# ave_error = total_error / len(x_vel)

# for a in range(len(x_vel)):
#     x_vel[a] = x_vel[a] - ave_error*a


plt.figure("x_acc")
plt.xlabel("Tid (s)")
plt.ylabel("Acceleration (g m/s^2)")
plt.plot(t_x, x_acc)

plt.figure("x_vel")
plt.xlabel("Datapunkt")
plt.ylabel("Hastighet (g m/s)")
plt.plot(t_x, x_vel)

# plt.figure("z_acc")
# plt.xlabel("Datapunkt")
# plt.ylabel("Acceleration (g m/s^2)")
# plt.plot(z_acc)

plt.show()