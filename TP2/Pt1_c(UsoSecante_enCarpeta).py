import numpy as np
x_1 = 0.598
funcion_1 = (x_1**(-1)) - np.tan(x_1)

x_2 = 0.659
funcion_2 = (x_2**(-1)) - np.tan(x_2)

solucion = x_2 - funcion_2 *(x_2-x_1)/(funcion_2-funcion_1)
print(solucion)