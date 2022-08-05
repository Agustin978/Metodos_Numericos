import numpy as np

def f(x):
    return (1 + x**2)**(-0.5)

def TrapecioCompuesta(a,b,h,n):
    x = np.zeros([n+1])
    x[0] = a
    x[n] = b
    suma = 0
    for i in np.arange(1,n):
        x[i] = x[i - 1] + h
        suma += f(x[i])
    integralTC = (h/2) * (f(x[0]) + 2 * suma + f(x[n]))
    return integralTC

def SimpsonCompuesta(a,b,h,n):
    x = np.zeros([n+1])
    x[0] = a
    x[n] = b
    sumaPar = 0
    sumaImpar = 0
    for i in np.arange(1,n):
        x[i] = x[i-1] + h
        if i%2==0:
            sumaPar += f(x[i])
        else:
            sumaImpar += f(x[i])
    
    integralSC = (h/3) * (f(x[0]) + 4 * sumaImpar + 2 * sumaPar + f(x[n]))
    return integralSC

def iteradorTC(a,b,inc):
    error_ant = 0
    n = inc
    h = (b-a)/n
    error = TrapecioCompuesta(a,b,h,n)
    iteracion = 0
    while round(error,6)!=round(error_ant,6):
        iteracion+=1
        error_ant = error
        n+=inc
        h = (b-a)/n
        error = TrapecioCompuesta(a,b,h,n)
        print("\nIteracion {}:\nValor: {}".format(iteracion, error))

def iteradorSC(a,b,inc):
    error_ant = 0
    n = inc
    h = (b-a)/n
    error = SimpsonCompuesta(a,b,h,n)
    iteracion = 0
    while round(error,6)!=round(error_ant,6):
        iteracion+=1
        print("Iteracion {}:\nValor: {}".format(iteracion, error))
        error_ant = error
        n += inc
        h = (b-a)/n
        error = SimpsonCompuesta(a,b,h,n)

print("\n================Trapecio Compuesta================")
iteradorTC(0,4,2)

print("\n================Simpson Compuesta================")
iteradorSC(0,4,2)