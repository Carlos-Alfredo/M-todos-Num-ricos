import matplotlib.pyplot as plt
import numpy as np
x1 = np.arange(0,9,1)
x2 = np.arange(0,9,1)
x3 = np.arange(0,9,1)
x4 = np.arange(0,9,1)
y1 = (14-1.2*x1)/2.25
y2 = (8-x2)/1.1
y3 = 9-2.5*x3
y4 = (9.3-1.75*x4)/1.25
plt.plot(y1,x1)
plt.plot(y2,x2)
plt.plot(y3,x3)
plt.plot(y4,x4)
plt.rcParams["figure.figsize"] = (50,50)
plt.show()