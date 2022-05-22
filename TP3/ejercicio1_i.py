import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2,150)

f1 = (5-3*x)/2
f2 = (5.1-3.1*x)/2
f3 = (5.001-3*x)/2
f4 = (5.1-3.1*x)/2

plt.figure(1,(12,8),55,'w','g')
plt.subplot(1,1,1)
plt.plot(x, f1)
plt.plot(x, f2)
plt.plot(x, f3)
plt.plot(x, f4)
plt.show()