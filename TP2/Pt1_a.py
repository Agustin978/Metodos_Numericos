import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.5, 1.5, 150)

funcion = (x**(-1)) - np.tan(x)

plt.figure(1,(12,8),55,'w','g')
plt.subplot(2,1,1)
plt.plot(x, funcion)
plt.show()