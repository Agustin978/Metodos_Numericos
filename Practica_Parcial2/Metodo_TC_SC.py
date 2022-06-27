from errno import ECHILD
from re import A, I, T
import numpy as np


def f(x):
    return x * np.cos(x**2)

def f2(x): #Derivada segunda de la funcion
    return (-6 * x * np.sin(x**2)) - (4 * x**3 * np.cos(x**2))

def f4(x): #Derivada 4 de la funcion
    return (-60 * x * np.cos(x**2)) + (80 * x**3 * np.sin(x**2)) + (16 * x**5 * np.cos(x**2))

def TrapecioCompuesta(a,b,n):
    h = (b-a)/n #Calculo de la separacion entre los puntos
    x = np.zeros([n+1]) #Arreglo donde se guardaran los puntos que delimitan los subintervalos
    x[0] = a
    x[n] = b
    suma = 0

    for i in np.arange(1,n):
        x[i] = x[i-1] + h #Ingreso el valor del siguiente punto de la tabla
        #Por ejemplo, para la primera iteracion tengo que x[1] = x[1-1] + h => a + h
        #print("\nValor de X[i]: {}".format(x[i]))
        suma += f(x[i])
    
    integralTC = (h/2) * (f(x[0]) + 2 * suma + f(x[n]))

    return integralTC

def SimpsonCompuesta(a,b,n):
    h = (b-a)/n #Calculo de la separacion entre los puntos
    x = np.zeros([n+1]) #Arreglo donde guardo los puntos que voy calculando
    x[0] = a #Primer elemento del arreglo a
    x[n] = b #Ultimo elemento del arreglo b
    sumaPar = 0
    sumaImpar = 0
    
    for i in np.arange(1,n): #Para recorrer el arreglo desde la posicion 1 hasta n
        x[i] = x[i-1] + h #Ingreso el valor del siguiente punto de la tabla
        #Por ejemplo, para la primera iteracion tengo que x[1] = x[1-1] + h => a + h
        if(i%2 == 0): #Determino si la posicion de x a calcular es par o impar
            sumaPar += f(x[i])
        else:
            sumaImpar += f(x[i])
        
    integralSC = (h/3) * (f(x[0]) + 4 * sumaImpar + 2 * sumaPar + f(x[n])) 
    #Calculo de la integral simpson compuesta
    return integralSC

def ErrorTC(a, b, precision):
    n = 2
    iterador = 0 #Cuenta las iteraciones
    error = 2 * precision #Se repetira el bucle hasta que el error se aproxime a la precision
    while np.abs(error) > precision:
        iterador+=1
        print("\nIteracion {}:".format(iterador))
        valorTC = TrapecioCompuesta(a,b,n) #Calculo del valor de trapecio compuesta
        h = (b-a)/n
        error = - ((((b-a) * h**2))/12) * f2(b)
        print("\nCalculo de TC = {}\nError = {}".format(valorTC, np.abs(error)))
        n+=2

    if np.abs(error) <= precision:
        print("\nEl calculo de TC con una precision de {} obtenido es:".format(precision))
        print("\nTC = {}\nError = {}\n".format(valorTC, np.abs(error)))

def ErrorSC(a,b,precision):
    n = 2
    iterador = 0 #Cuenta las iteraciones realizadas
    #h = (b-a)/n
    error = 2 * precision
    error_ant = 0
    while np.abs(error) > precision: #El bucle se repetira hasta que dos aproximaciones sucesivas sean del orden de la precision
        iterador += 1
        print("\nIteracion {}:".format(iterador))
        valorSC = SimpsonCompuesta(a,b,n)
        h = (b-a)/n
        error = -(((b-a)*h**4)/180) * f4(b)
        print("\nCalculo de SC = {}\nError = {}".format(valorSC, np.abs(error)))
        error_ant = error
        n+=2
    
    if np.abs(error) <= precision:
        print("\nEl calculo de SC con una precision de {} obtenido es:".format(precision))
        print("\nSC = {}\nError = {}\nError iteracion anterior = {}".format(valorSC, np.abs(error), np.abs(error_ant)))
        

#Itc = TrapecioCompuesta(0.0, 4.0, 4)

#ErrorTC(0.0, 4.0, 0.000001)

#Isc = SimpsonCompuesta(0.0, 4.0, 4)
#print("Valor de SC = {}".format(Isc))

ErrorSC(0.0, 4.0, 0.000001)