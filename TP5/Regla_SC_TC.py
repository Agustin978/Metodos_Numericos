from msilib.schema import AppSearch
import numpy as np

#Funcion a integrar
def f(x):
    return x * np.cos(x**2)

#Derivada segunda de la funcion (Utilizada para calculo del error en Trapecio Compuesta)
def f2(x):
    return (-6 * x * np.sin(x**2)) - (4 * x**3 * np.cos(x**2))

#Derivada cuarta de la funcion (Utilizada para calculo del error en Simpson Compuesta)
def f4(x):
    return (-60 * x * np.cos(x**2)) + (80 * x**3 * np.sin(x**2)) + (16 * x**5 * np.cos(x**2))
"""

def f(x):
    return x**7 - 15 * x**3 + 10 * x + 20

def f4(x):
    return 840 * x**3
"""

def SimpsonCompuesta(a,b,n,h):
    x = np.zeros([n+1]) #Siendo n la cantidad de subintervalos
    #h = (b-a)/n
    x[0] = a
    x[n] = b
    sumaPar = 0
    sumaImpar = 0
    
    for i in np.arange(1,n):
        x[i] = x[i-1] + h
        if i%2 == 0:
            sumaPar = sumaPar + f(x[i])
        else:
            sumaImpar = sumaImpar + f(x[i])
    
    integralSC = (h/3)*(f(x[0])+4*sumaImpar+2*sumaPar+f(x[n]))
    return integralSC

def TrapecioCompuesta(a,b,n,h):
    x = np.zeros([n+1])
    #h = (b-a)/n
    x[0] = a
    x[n] = b
    suma = 0

    for i in np.arange(1,n):
        x[i] = x[i-1] + h
        suma = suma + f(x[i])
    
    integralTC = (h/2) * (f(x[0]) + 2 * suma + f(x[n]))
    
    return integralTC


#Funcion para las iteraciones y calculo del error
def iteradorSC(a,b,eps):
    n = 2
    iteracion = 0
    eta = b
    #h = (b-a)/n
    error_ant = 2
    while np.abs(error_ant) > eps:
        h = (b-a)/n
        error = - (((b-a) * h**4) / 180) * f4(eta)
        error_ant = error
        iteracion += 1
        print("\nIteracion: {} / Simpson Compuesta: {} / Error: {}".format(iteracion, SimpsonCompuesta(a,b,n,h), np.abs(error)))
        n += 2
    
    if np.abs(error_ant) <= eps:
        print("\nIteracion Final: {} / Simpson Compuesta: {} / Error: {}\n".format(iteracion, SimpsonCompuesta(a,b,n,h), error))

def iteradorTC(a,b,eps):
    n = 2
    iteracion = 0
    eta = b
    h = (b-a)/n
    error = - (((b-a) * h**2) / 12) * f2(eta)
    while np.abs(error) > eps:
        h = (b-a)/n
        error = - (((b-a) * h**2) / 12) * f2(eta)
        iteracion += 1
        print("\nIteracion: {} / Simpson Compuesta: {} / Error: {}".format(iteracion, TrapecioCompuesta(a,b,n,h), np.abs(error)))
        n += 2
    
    if np.abs(error) <= eps:
        print("\nIteracion Final: {} / Simpson Compuesta: {} / Error: {}".format(iteracion, TrapecioCompuesta(a,b,n,h), np.abs(error)))

print("\n\n=============Simpson Compuesta=============")
iteradorSC(0, np.pi, 0.000001)


print("\n\n=============Trapecio Compuesta=============")
iteradorTC(0, np.pi, 0.000001)
#iteradorN(0, 2, 0.000001)
    




