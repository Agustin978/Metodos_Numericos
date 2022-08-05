from ftplib import error_perm
import numpy as np


def f(x):
    return x * np.cos(x**2)

#Derivada segunda de la funcion (Utilizada para calculo del error en Trapecio Compuesta)
def f2(x):
    return (-6 * x * np.sin(x**2)) - (4 * x**3 * np.cos(x**2))

#Derivada cuarta de la funcion (Utilizada para calculo del error en Simpson Compuesta)
def f4(x):
    return (-60 * x * np.cos(x**2)) + (80 * x**3 * np.sin(x**2)) + (16 * x**5 * np.cos(x**2))

#===================Metodo Simpson Compuesta
def SimpsonCompuesta(a, b, n, h):
    x = np.zeros([n+1])
    x[0] = a
    x[n] = b
    sumaPar = 0
    sumaImpar = 0
    i = 1
    for i in range(n):
        x[i] = x[i-1] + h
        if i%2 == 0:
            sumaPar = sumaPar + f(x[i])
        else:
            sumaImpar = sumaImpar + f(x[i])
    
    integralSC = (h/3) * (f(x[0]) + 4*sumaImpar + 2*sumaPar + f(x[n]))
    return integralSC

def TrapecioCompuesta(a , b, n, h):
    x = np.zeros([n+1])
    x[0] = a
    x[n] = b
    suma = 0
    for i in np.arange(1,n):
        x[i] = x[i-1] + h
        suma = suma + f(x[i])
    integralTC = (h/2)*(f(x[0]) + 2 * suma + f(x[n]))
    return integralTC

def iteradorSC(a, b):
    n = 2
    iteracion = 0
    error_ant = 0
    h = (b-a)/n
    error = np.abs(SimpsonCompuesta(a, b, n, h) - error_ant)
    while round(error,6) != round(error_ant,6):
        error_ant = error
        h = (b - a)/n
        error = SimpsonCompuesta(a, b, n, h)
        iteracion += 1
        print("\nIteracion {}:\nSimpson Compuesta: {}\n".format(iteracion, SimpsonCompuesta(a , b, n, h)))
        n += 2

def iteradorTC(a,b):
    n = 1
    iteracion = 0
    #eta = b
    #error = 2 * eps
    error_ant = 0
    h = (b - a)/n
    error = np.abs(TrapecioCompuesta(a,b,n,h))
    while round(error,6) != round(error_ant,6):
        #error = np.abs(-(((b-a) * h**2)/12) * f2(eta))
        iteracion += 1
        print("\nIteracion {}:\nTrapecio Compuesta: {}\n".format(iteracion, TrapecioCompuesta(a, b, n, h)))
        error_ant = error
        n += 1
        h = (b - a)/n
        error = np.abs(TrapecioCompuesta(a,b,n,h))


print("\n========================Simpson Compuesta========================")
iteradorSC(0, np.pi)

print("\n========================Trapecio Compuesta========================")
iteradorTC(0, np.pi)