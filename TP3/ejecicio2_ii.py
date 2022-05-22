import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2,150)

f1 = (2-2*x)/3
f2 = (1.999-1.999*x)/3
f3 = (2-2*x)/3
f4 = (2-1.999*x)/3

plt.figure(1,(12,8),55,'w','g')
plt.subplot(1,1,1)
plt.plot(x, f1)
plt.plot(x, f2)
plt.plot(x, f3)
plt.plot(x, f4)
plt.show()