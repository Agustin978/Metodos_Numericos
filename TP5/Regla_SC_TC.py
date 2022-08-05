from msilib.schema import AppSearch
import numpy as np
"""
#Ejercicio 3a)
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
"""
#Ejercicio 3b)
#Funcion a integrar
def f(x):
    return x**2 * np.cos(x)

#Derivada segunda de la funcion (Utilizada para calculo del error en Trapecio Compuesta)
def f2(x):
    return (2 * np.cos(x)) - (4 * x * np.sin(x)) + (x**2 * np.cos(x))

#Derivada cuarta de la funcion (Utilizada para calculo del error en Simpson Compuesta)
def f4(x):
    return (- 8 * np.cos(x)) - (x**2 * np.cos(x))
"""
"""
#Ejercicio 4a)
#Funcion a integrar
def f(x):
    return np.sin(10*x)

#Derivada segunda de la funcion (Utilizada para calculo del error en Trapecio Compuesta)
def f2(x):
    return - np.sin(10 * x) * 100
"""
"""
#Ejercicio 4b)
#Funcion a integrar
def f(x):
    return np.exp(x**2)

#Derivada segunda de la funcion (Utilizada para calculo del error en Trapecio Compuesta)
def f2(x):
    return (2 * np.exp(x**2)) + (4 * x**2 * np.exp(x**2))
"""

#Ejercicio 4c)
#Funcion a integrar
def f(x):
    return np.log(np.exp(x))

#Derivada segunda de la funcion (Utilizada para calculo del error en Trapecio Compuesta)
def f2(x):
    return -(1/x**2)


#========================================METODOS========================================
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
    error = 2 * eta
    while error > eps:
        h = (b-a)/n
        error = np.abs((((b-a) * h**4) / 180) * f4(eta)) #Cota de error
        #error = SimpsonCompuesta(a,b,n,h) - val_ant
        iteracion += 1
        print("\nIteracion: {} / Simpson Compuesta: {} / Error: {}".format(iteracion, SimpsonCompuesta(a,b,n,h), np.abs(error)))
        n += 2
    
    if np.abs(error) <= eps:
        print("\nIteracion Final: {} / Simpson Compuesta: {} / Error: {}\n".format(iteracion, SimpsonCompuesta(a,b,n,h), error))

def iteradorTC(a,b,eps):
    n = 1
    iteracion = 0
    eta = b
    h = (b-a)/n
    #error = - (((b-a) * h**2) / 12) * f2(eta) #Cota de error
    error = 2 * eps
    while error > eps:
        h = (b-a)/n
        error = np.abs((((b-a) * h**2) / 12) * f2(eta))
        #error = TrapecioCompuesta(a,b,n,h) - val_Ant
        #val_Ant = TrapecioCompuesta(a,b,n,h)
        iteracion += 1
        print("\nIteracion: {} / Trapecio Compuesta: {} / Error: {}".format(iteracion, TrapecioCompuesta(a,b,n,h), np.abs(error)))
        n += 1
    
    if np.abs(error) <= eps:
        print("\nIteracion Final: {} / Trapecio Compuesta: {} / Error: {}".format(iteracion, TrapecioCompuesta(a,b,n,h), np.abs(error)))

#print("\n\n=============Simpson Compuesta=============")
#iteradorSC(0, np.pi, 0.000001) #Para ejercicio 3a y 3b


print("\n\n=============Trapecio Compuesta=============")
#iteradorTC(0, np.pi, 0.000001)
#iteradorTC(0, 2, 0.000001) #Ejerciocio 4a
#iteradorTC(0,1,0.000001) #Ejercicio 4b
iteradorTC(1,10,0.000001) #Ejercicio 4c