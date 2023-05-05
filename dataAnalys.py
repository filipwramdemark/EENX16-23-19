import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import find_peaks

p = []

testfile = "tests/test2/test1.csv"

data = pd.read_csv(testfile).values.tolist()

x_data = []
z_data = []
x_time = []
z_time = []

t0 = data[0][1]

for i in range(len(data)):
    if abs(data[i][0]) < 100000:
        if i % 2 == 0:
            x_data.append(data[i][0])
            x_time.append(data[i][1] - t0)
        else: 
            z_data.append(data[i][0])
            z_time.append(data[i][1] - t0)

location, props = find_peaks(x_data, height=3.5)
peaks = props["peak_heights"]

plt.figure(1)
plt.plot(x_time, x_data)
plt.plot([x_time[i] for i in range(len(x_time)) if i in location], peaks, 'o')
plt.show()



plt.figure(2)
plt.grid(True)
# plt.set_title(testfile)

curveFit = []
curveFitTime = []

for a in range(len(location)):
    testCut = []
    for i in range(location[a] - 8, location[a] + 9):
        testCut.append(x_data[i])
    xNew = np.linspace(0, len(testCut), len(testCut))
    curveFitTime.extend(xNew)
    curveFit.extend(testCut)
    plt.plot(xNew, testCut)

p1 = np.polyfit(curveFitTime, curveFit, 6)
x1 = np.linspace(min(curveFitTime), max(curveFitTime), 1000)
y1 = np.polyval(p1, x1)
plt.plot(x1, y1, 'r', linewidth=3)

offset = 1.5


plt.plot(x1, y1 + offset, '--b', linewidth=1.5)
plt.plot(x1, y1 - offset, '--b', linewidth=1.5)

count1 = 0

for i in range(len(curveFit)):
    if curveFit[i] < (np.polyval(p1, curveFitTime[i]) - offset):
        count1 += 1
        plt.plot(curveFitTime[i], curveFit[i], 'x', markersize=5, linewidth=1.5)
    elif curveFit[i] > (np.polyval(p1, curveFitTime[i]) + offset):
        count1 += 1
        plt.plot(curveFitTime[i], curveFit[i], 'x', markersize=5, linewidth=1.5)

percentage1 = count1 / len(curveFit)
print("Part 1 percentage: ")
print(percentage1)

plt.show()