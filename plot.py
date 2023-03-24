import matplotlib.pyplot as plt
import pandas as pd

y=pd.read_csv('x_acc.csv')
plt.plot(y)
plt.show()