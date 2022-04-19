import re
import numpy as np
import math
#import sympy as sp
#------------DECLARACION DE LA FUNCION Y SU DERIVADA------------
def f(x):
    return pow(x, 3) - x

def df(x):
    return 3*pow(x,2)-1

#------------METODO DE BISECCION------------(CORREGIDO)
def Biseccion(a, b, eps, intMax):
    i = 0
    valMed = (a+b)/2

    while i<=intMax and np.abs(f(valMed))>eps:
        error = np.abs(a-valMed)
        if f(a)*f(valMed)>0:
            a = valMed
        else:
            b = valMed
        print('Valor en iteracion {}: {} / error: {}'.format(i+1,valMed, error))
        valMed = (a+b)/2
        i+=1
    
    if i>intMax:
        print('No converge en el numero de iteraciones ingresado: {}'.format(intMax))
        return 0
    else:
        print('Raiz: {}'.format(valMed))
        return valMed

#------------METODO REGULAFALSI------------(CORREGIDO)
def RegulaFalsi(a,b, eps, intMax):
    i=1
    x = b-((f(b)*(b-a))/(f(b)-f(a)))

    while i<=intMax and np.abs(f(x))>eps:
        if f(a)*f(x)>0:
            a = x
        else:
            b = x
        x = b-((f(b)*(b-a))/(f(b)-f(a)))
        print('Numero de iteraciones {}: {}'.format(i, x))
        i+=1
    
    if i>intMax:
        print('No converge en el numero de iteraciones ingresado: {}'.format(intMax))
        return 0
    else:
        print('Raiz: {}'.format(x))
        return x

#------------METODO DE LA SECANTE------------
def Secante(a,b,eps,itMax):
    i = 0 
    x_n_1 = a
    x_n = b
    x_n1 = x_n - (f(x_n) * ((x_n - x_n_1)/(f(x_n) - f(x_n_1))))
    while i<=itMax and np.abs(x_n1-x_n)>eps:
        x_n_1 = x_n
        x_n = x_n1
        error = np.abs(x_n_1 - x_n)
        print('Valor en iteracion {}: {} / error: {}'.format(i+1,x_n1, error))
        x_n1 = x_n - (f(x_n) * ((x_n - x_n_1)/(f(x_n) - f(x_n_1))))
        i+=1
    
    if i>itMax:
        print('No converge en el numero de iteraciones ingresado: {}'.format(itMax))
        return 0
    else:
        print('Raiz: {}'.format(x_n1))
        return x_n1
    
#------------Metodo Newton-Raphson------------
"""
def NewtonRaphson(x,eps,intMax):
    i=0
    x_1 = x + 2*eps

    while i<=intMax and np.abs(x_1-x)>eps:
        x_1 = x - (f(x))
"""

#------------Metodo de Iteracion de Punto Fijo------------
def PuntoFijo(x, eps, itMax):
    for i in range(itMax):
        x_1 = f(x)
        if np.abs(x_1-x)<eps:
            error = np.abs(x_1-x)
            print('Iteracion donde converge {}, Valor del punto fijo: {} // ERROR: {}'.format(i+1, x_1, error))
            return
        error = np.abs(x_1-x)
        print('Valor de iteracion {}: {} // ERROR: {}'.format(i+1, x_1, error))
        x = x_1
        
    if i+1==itMax:
            print('El metodo no converge en el numero de iteraciones dado. Intente nuevamente con un numero mayor de iteraciones')


print('\n\n')

print('====Metodo de Biseccion====')
sol_1 = Biseccion(0.5, 1.5, 0.001, 150)
print(sol_1)

print('\n\n')

print('====Metodo Regula Falsi====')
sol_2 = RegulaFalsi(0.5, 1.5, 0.001, 100)
print(sol_2)

print('\n\n')

print('====Metodo Secante====')
sol_3 = Secante(0.5, 1.5, 0.001, 150)
print(sol_3)


#------------Metodo de Iteracion de Punto Fijo------------
print('\n\n')

print('===Metodo de Iteracion de Punto Fijo===')
PuntoFijo(0, 0.0001, 150)