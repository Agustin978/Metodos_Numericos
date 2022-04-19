import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 150)

funcion_1 = x**2 - 2*x -3
funcion_2 = np.sqrt((2*x)+3)
funcion_3 = ((x**2)-3)/2
funcion_4 = 3/(x-2)

plt.figure(1,(12,8),55,'w','g')
plt.subplot(2,1,1)
plt.plot(x, funcion_1)
plt.plot(x, funcion_2)
plt.plot(x, funcion_3)
plt.plot(x, funcion_4)
plt.show()