from distutils.log import error
from re import S
from tkinter import W
import numpy as np
from sklearn.utils import column_or_1d
from sympy import false

#A = np.loadtxt('TP3/A.txt', delimiter=',')
#B = np.loadtxt('TP3/b.txt', delimiter=',')
#X = np.loadtxt('TP3/X.txt', delimiter=',')

#A = np.array([[2,-1,0],[1,6,-2],[4,-3,8]])
#B = np.array([2,-4,5])
#X = np.zeros(3)

A = np.array([[6,-2,1],[-2,7,2],[1,2,-5]])
B = np.array([4,1,-4.5])
X = np.zeros(3)

#=================Metodo Gauss-Seidel

def Gauss_Seidel2(A,B,X,iteraTot):
    #X = np.zeros(3)
    k = 0
    #filas, columnas = np.shape(A)
    for k in range(iteraTot):
        print("\nIteracion {}".format(k+1))
        X[0] = (B[0]-A[0,1]*X[1]-A[0,2]*X[2])/A[0,0]
        X[1] = (B[1]-A[1,0]*X[0]-A[1,2]*X[2])/A[1,1]
        X[2] = (B[2]-A[2,0]*X[0]-A[2,1]*X[1])/A[2,2]
        print("X = {}".format(X))
        error = np.linalg.norm(np.dot(A,X)-B)
        print("Error = {}".format(error))
    
    print("\n\n")
    print("La matriz solucion final con {} iteraciones es:".format(iteraTot))
    print("x1 = {}".format(X[0]))
    print("x2 = {}".format(X[1]))
    print("x3 = {}".format(X[2]))
    print("El error final es: {}".format(error))

#=================Metodo Gauss-Seidel (El metodo funcional)====================================
def Gauss_Seidel(A,B,X,iteraTot,precision):
    k = 0
    error = 2 * precision
    tamanio = np.shape(A)
    filas = tamanio[0]
    columnas = tamanio[1]
    diferencia = np.ones(filas, dtype= float)
    while error > precision and k < iteraTot:
        k+=1
        print('Iteracion {}:'.format(k))
        for f in range(filas):
            suma = 0
            for c in range(columnas):
                if f!=c:
                    suma = suma+ A[f,c]*X[c]
                
            nuevo = (B[f] - suma)/A[f,f]
            diferencia[f] = np.abs(nuevo - X[f])
            X[f] = nuevo
        error = np.max(diferencia)
        print("X = {}\nError: {}".format(X, error))

    if error == precision or error < precision:
        print("El valor final de X con una precision de {} es:".format(precision))
        print("X = {}".format(X))
        print("EL error es: {}".format(error))
        print("Se obtuvo en la iteracion {}".format(k))
    elif k == iteraTot:
        print("El valor final obtenido de X con {} iteraciones es:".format(k))
        print("X = {}".format(X))
        print("El error obtenido es: {}".format(error))

#======================== Metodo Jacobi =================================

def Jacobi(A,B,X,iteraTot, precision):
    k = 0
    error = 2 * precision
    tamanio = np.shape(A)
    filas = tamanio[0]
    columnas = tamanio[1]
    diferenciaErr = np.zeros(filas, dtype= float)
    Xi = np.zeros(filas) #Vector donde se guardaran los resultados
    while error > precision and k < iteraTot:
        k += 1
        print("Iteracion {}:".format(k))
        for f in range(filas):
            nuevo = B[f]
            for c in range(columnas):
                if(f!=c):
                    nuevo = nuevo - A[f,c]*X[c]
            nuevo = nuevo / A[f,f]
            #X[f] = (B[f] - X[f])/A[f,f]
            Xi[f] = nuevo
            diferenciaErr[f] = np.abs(X[f] - Xi[f])
            error = np.max(diferenciaErr)
            X[f] = Xi[f]
        print("X = {}".format(X))
        print("Error: {}\n".format(error))
    
    if error == precision or error < precision:
        print("El valor final de X con una precision de {} es:".format(precision))
        print("X = {}".format(X))
        print("EL error es: {}".format(error))
        print("Se obtuvo en la iteracion {}".format(k))
    elif k == iteraTot:
        print("El valor final obtenido de X con {} iteraciones es:".format(k))
        print("X = {}".format(X))
        print("El error obtenido es: {}".format(error))


#======================== Metodo de SOR =================================
def Sor(A, b, omega, X, precision, itMax):
    Xi = X[:]
    error = np.linalg.norm(np.matmul(A, Xi) - b) #Calculo de error inicial
    k = 0
    while error > precision and k < itMax:
        print("\nIteracion {}:".format(k+1))
        for i in range(A.shape[0]):
            sigma = 0
            for j in range(A.shape[1]):
                if j != i:
                    sigma += A[i][j] * Xi[j]
            Xi[i] = (1 - omega) * Xi[i] + (omega / A[i][i]) * (b[i] - sigma)
        error = np.linalg.norm(np.matmul(A, Xi) - b)
        print("X = {}".format(Xi))
        print('Error: {0:10.6g}\n'.format(error))
        k += 1
    
    if error == precision or error < precision:
        print("El valor final de X con una precision de {} es:".format(precision))
        print("X = {}".format(Xi))
        print("EL error es: {}".format(error))
        print("Se obtuvo en la iteracion {}".format(k))
    elif k == itMax:
        print("El valor final obtenido de X con {} iteraciones es:".format(k))
        print("X = {}".format(Xi))
        print("El error obtenido es: {}".format(error))



print("\n\n============Metodo Gauss-Seidel============")
Gauss_Seidel(A,B,X,20,0.001)

#print("\n\n============Metodo Jacobi============")
#Jacobi(A,B,X,20,0.001)

#print("\n\n============Metodo de SOR============")
#Sor(A, B, 0.5, X, 0.000001, 200)