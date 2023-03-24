import matplotlib.pyplot as plt
import pandas as pd
import scipy.integrate as it
import statistics

acc = pd.read_csv('x_acc.csv').values.tolist()

acc = [x[0] for x in acc]
# vel = []

# for i,a in enumerate(acc):
#     if i > 0:
#         sum = vel[i-1]
#     else:
#         sum = 0
#     new_sum = sum + a
#     vel.append(new_sum)

vel = it.cumtrapz(acc, initial=0)

print(vel[0:50])
plt.plot(acc)
plt.plot(vel)
plt.show()