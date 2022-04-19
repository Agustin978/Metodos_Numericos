from distutils.log import error
import numpy as np
import math

#------------DECLARACION DE LA FUNCION Y SU DERIVADA------------

def f(x):
    return 3/(x-2)

def f_1(x):
    return pow(x, 3) - x

def df(x):
    return 3*pow(x,2)-1

#------------METODO REGULAFALSI------------
def RegulaFalsi(a,b,eps,itMax):
    i = 0
    x = b - ((f(b)*(b-a))/(f(b)-f(a)))

    while i<=itMax and np.abs(f(x)>eps):
        
        if f(a)*f(x)>0:
            a=x
        else:
            b=x
        print('Valor en iteracion {}: {}'.format(i+1,x))
        x = b - ((f(b)*(b-a))/(f(b)-f(a)))
        i += 1
    
    if i > itMax:
        print('El metodo no converge en el numero de iteraciones dado. Intente nuevamente con un numero mayor de iteraciones')
    else:
        print('Raiz: {}'.format(x))

#------------METODO DE BISECCION------------
def Biseccion(a,b,eps,itMax):
    i = 0
    valMed = (a+b)/2
    
    while i<=itMax and np.abs(f(valMed))>eps:
        error = np.abs(a-valMed)
        if f(a)*f(valMed)>0:
            a = valMed
        else:
            b = valMed
        print('Valor en iteracion {}: {} / error: {}'.format(i+1,valMed, error))
        valMed = (a+b)/2
        i += 1
    
    if i > itMax:
        print('El metodo no converge en el numero de iteraciones dado. Intente nuevamente con un numero mayor de iteraciones')
    else:
        print('Raiz: {}'.format(valMed))

#------------METODO DE LA SECANTE------------
def Secante(a,b,eps,itMax):
    i = 0 
    x_n_1 = a
    x_n = b
    #x_n1 = 2*x_n
    x_n1 = x_n - (f(x_n) * ((x_n - x_n_1)/(f(x_n) - f(x_n_1))))

    while i<=itMax and np.abs(x_n1-x_n)>eps:
        x_n_1 = x_n
        x_n = x_n1
        error = np.abs(x_n_1 - x_n)
        print('Valor en iteracion {}: {} / error: {}'.format(i+1,x_n1, error))
        x_n1 = x_n - (f(x_n) * ((x_n - x_n_1)/(f(x_n) - f(x_n_1))))
        i+=1
    
    if i>itMax:
        print('El metodo no converge en el numero de iteraciones dado. Intente nuevamente con un numero mayor de iteraciones')
    else:
        print('Raiz: {}'.format(x_n1))
    
#------------METODO NEWTON-RAPHSON------------
def NewtonRaphson(x,eps,itMax):
    i=0
    #x_1 = x + 2*eps
    x_1 = x - (f_1(x)/df(x))

    while i<=itMax and np.abs(x_1-x)>eps:
        error = np.abs(x_1-x)
        print('Valor en iteracion {}: {} / error: {}'.format(i+1,x_1, error))
        x = x_1
        x_1 = x - (f_1(x)/df(x))
        i+=1
    
    if i>itMax:
        print('El metodo no converge en el numero de iteraciones dado. Intente nuevamente con un numero mayor de iteraciones')
    else:
        print('Raiz: {}'.format(x_1))

#------------Metodo de Iteracion de Punto Fijo------------
"""
def PuntoFijo(x, eps, itMax):
    i = 1
    x_1 = f(x)
    while i<=itMax and np.abs(x_1-x)>eps:
        #x_1 = f(x)
        error = np.abs(x_1-x)
        print('Valor de iteracion {}: {} // ERROR: {}'.format(i, x_1, error))
        i += 1
        x_1 = f(x)
        x = x_1
    
    if i>itMax:
        print('El metodo no converge en el numero de iteraciones dado. Intente nuevamente con un numero mayor de iteraciones')
    else:
        print('Raiz: {}'.format(x_1))

"""
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

    



#------------METODO REGULAFALSI------------
print('\n\n')

print('====Metodo Regula Falsi====')
RegulaFalsi(0.5, 1.5, 0.00001, 150)

#------------METODO DE BISECCION------------
print('\n\n')

print('====Metodo de Biseccion====')
Biseccion(0.5, 1.5, 0.00001, 150)

#------------METODO DE LA SECANTE------------
print('\n\n')

print('====Metodo de la Secante====')
Secante(0.5, 1.5, 0.00001, 150)

#------------METODO NEWTON-RAPHSON------------
print('\n\n')

print('====Metodo de Newton-Raphson====')
NewtonRaphson(np.sqrt(1/5), 0.0001, 150)

#------------Metodo de Iteracion de Punto Fijo------------
print('\n\n')

print('===Metodo de Iteracion de Punto Fijo===')
PuntoFijo(0, 0.0001, 150)