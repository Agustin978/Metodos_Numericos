import numpy as np
x = np.array([(1/3)**0.5, -((1/3)**0.5)])
w = np.array([1,1])
def f(x):
    return 0.2 + 25*x - 200 * x**2 + 675 * x**3 - 900 * x**4 + 400 * x**5

def CuadraturaGauss(b,a,x,w,n):
    suma = 0
    for i in range(n):
        suma = suma + w[i] * f((((b-a)*x[i])/2)+(b+a)/2)
    return ((b-a)/2) * suma

print("\n==============Cuadratura de Gauss-Legendre==============\n")
print("Valor de la integral usando Cuadratura de Gauss-Legendre: {}".format(CuadraturaGauss(0, 0.8, x, w, 2)))