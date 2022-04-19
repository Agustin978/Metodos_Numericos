import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 150)

funcion = x**2 - 2*x -3

plt.figure(1,(12,8),55,'w','g')
plt.subplot(2,1,1)
plt.plot(x, funcion)
plt.show()