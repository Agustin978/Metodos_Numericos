from distutils.log import error
import numpy as np
from sympy import difference_delta

A = np.loadtxt('TP3/A.txt', delimiter=',')
B = np.loadtxt('TP3/b.txt', delimiter=',')
X = np.loadtxt('TP3/X.txt', delimiter=',')

#=========================Metodo de Jacobi=========================
def Jacobi(A, B, X, iteraTot, precision):
    k = 0  #Determina las iteraciones que se realizen
    error = 2 * precision 
    tamanio = np.shape(A) #Obtengo las filas y columnas de la matriz
    filas = tamanio[0]
    columnas = tamanio[1]
    dif = np.zeros(filas, dtype=float) #Arreglo donde se guardan las diferencias entre el vector x anterior y el nuevo
    Xi = np.zeros(filas) #Arreglo donde se guardaran los nuevos valores de x
    while error > precision and k < iteraTot:
        k += 1
        print("\nIteracion {}:".format(k))
        for f in range(filas):
            nuevo = B[f]
            for c in range(columnas):
                if(f!=c):
                    nuevo = nuevo - A[f,c] * X[c]
            nuevo = nuevo / A[f,f]
            Xi[f] = nuevo
            dif[f] = np.abs(X[f] - Xi[f])
            X[f] = Xi[f]
        error = np.max(dif)
        print("X = {}".format(X))
        print("Error = {}\n".format(error))
    
    if error == precision or error < precision:
        print("\nEl valor final de X obtenido con una precision de {} es:".format(precision))
        print("X = {}".format(X))
        print("Error = {}".format(error))
        print("Cantidad de iteraciones: {}\n".format(k))
    elif k == iteraTot:
        print("\nEl valor final de X obtenido con un total de {} iteraciones es:".format(iteraTot))
        print("X = {}".format(X))
        print("Error = {}\n".format(error))

#=========================Metodo de Gauss-Seidel=========================
def Gauss_Seidel(A, B, X, iteraTot, precision):
    k = 0
    error = 2 * precision
    tamanio = np.shape(A)
    filas = tamanio[0]
    columnas = tamanio[1]
    dif = np.zeros(filas, dtype=float)
    #Xi = np.zeros(filas) No se requiere de una matriz extra, pues ira utilizando los nuevos valores que se vayan guardando
    while error > precision and k < iteraTot:
        k += 1
        print("\nIteracion {}:".format(k))
        for f in range(filas):
            suma = 0
            for c in range(columnas):
                if f != c:
                    suma = suma + A[f,c]*X[c]
            nuevo = (B[f] - suma) / A[f,f]
            dif = np.abs(nuevo - X[f])
            X[f] = nuevo
        error = np.max(dif)
        
        print("X = {}".format(X))
        print("Error = {}".format(error))

    if error == precision or error < precision:
        print("\nEl valor final de X obtenido con una precision de {} es:".format(precision))
        print("X = {}".format(X))
        print("Error = {}".format(error))
        print("Cantidad de iteraciones: {}\n".format(k))
    elif k == iteraTot:
        print("\nEl valor final de X obtenido con un total de {} iteraciones es:".format(iteraTot))
        print("X = {}".format(X))
        print("Error = {}\n".format(error))

#======================== Metodo de SOR =================================
def SOR(A, B, X, iteraTot, precision, omega): #Valor de omega entre 0 y 2
    k = 0
    error = 2 * precision
    tamanio = np.shape(A)
    filas = tamanio[0]
    columnas = tamanio[1]
    dif = np.zeros(filas, dtype=float)
    while error > precision and k < iteraTot:
        k += 1
        print("\nIteracion {}:".format(k))
        for f in range(filas):
            suma = 0
            for c in range(columnas):
                if(f != c):
                    suma = suma + A[f,c]*X[c]
            nuevo = ((omega * (B[f] - suma)) / A[f,f]) + (1 - omega) * X[f]
            dif[f] = np.abs(nuevo - X[f])
            X[f] = nuevo
        error = np.max(dif)
        print("X = {}".format(X))
        print("Error = {}\n".format(error))
    
    if error == precision or error < precision:
        print("\nEl valor final de X obtenido con una precision de {} es:".format(precision))
        print("X = {}".format(X))
        print("Error = {}".format(error))
        print("Cantidad de iteraciones: {}\n".format(k))
    elif k == iteraTot:
        print("\nEl valor final de X obtenido con un total de {} iteraciones es:".format(iteraTot))
        print("X = {}".format(X))
        print("Error = {}\n".format(error))

print("\n\n============Metodo Jacobi============")
Jacobi(A,B,X,20,0.001)

print("\n\n============Metodo Gauss-Seidel============")
Gauss_Seidel(A,B,X,20,0.000001)

print("\n\n============Metodo de SOR============")
SOR(A, B, X, 20, 0.000001, 0.5)