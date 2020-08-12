import matplotlib.pyplot as plt
import numpy as np
x1 = np.arange(0,550,1)
x2 = np.arange(0,550,1)
x3 = np.arange(0,550,1)
x4 = np.arange(0,550,1)
y1 = (40-0.04*x1)/0.12
y2 = 550-x2
y3 = (9500-20*x3)/5
y4 = (22250-45*x4)/20
plt.plot(y1,x1)
plt.plot(y2,x2)
plt.plot(y3,x3)
plt.plot(y4,x4)
plt.rcParams["figure.figsize"] = (50,50)
plt.show()