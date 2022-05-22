import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,4,150)

funcion_principal = x**2 + x - 1
funcion_g1 = 1 - x**2
funcion_g2 = np.sqrt( 1 - x )
funcion_g3 = 1 / (x+1)

plt.figure(1,(12,8),55,'w','g')
plt.subplot(2,1,1)
plt.plot(x,funcion_principal)
plt.plot(x,funcion_g1)
plt.plot(x,funcion_g2)
plt.plot(x,funcion_g3)


plt.show()