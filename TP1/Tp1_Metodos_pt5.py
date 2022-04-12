import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.999, 1.001, 150)
#suma_1 = x**8-8*(x**7)+28*(x**6)-56*(x**5)+70*(x**4)-56*(x**3)+28*(x**2)-8*x+1
suma_1 = x**8 - 8*x**7 + 28*x**6 - 56*x**5 + 70*x**4 - 56*x**3 +28*x**2 - 8*x + 1
print(suma_1)
suma_2 = (x-1)**8 
print(suma_2)

plt.figure(1,(12,8),55,'w','g')
plt.subplot(2,1,1)
plt.plot(x, suma_1)

plt.subplot(2,1,2)
plt.plot(x, suma_2)

plt.show()