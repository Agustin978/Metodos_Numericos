from cgi import print_environ
from ipaddress import collapse_addresses
import numpy as np

A = np.array([[2,-1,0],[1,6,-2],[4,-3,8]]) #Arreglo de terminos
B = np.array([2,-4,5]) #Arreglo de soluciones
X = np.zeros(3) #Arreglo de variables

#============Metodo de Jacobi============
def jacobi(A, B, X, iteraTot, precision):
    k = 0 #Iterador
    error = 2 * precision #La cantidad de iteraciones que se haran, dependera de la aproximacion que el error tenga a la precision
    tamanio = np.shape(A) #Obtengo filas y columnas de la matriz A
    filas = tamanio[0]
    columnas = tamanio[1]
    diferenciaErr = np.zeros(filas, dtype=float) #Creo un arreglo de 0s donde guardare los errores calculados en cada operacion
    Xi = np.zeros(filas) #Matriz donde guardo los resultados

    while error>precision and k < iteraTot:
        k+=1
        print("\nIteracion {}:".format(k))
        for f in range(filas): #Iterador de filas
            nuevo = 0
            for c in range(columnas):
                if(f!=c): #Quito la posibilidad de añadir Aii al calculo
                    nuevo = nuevo + A[f,c]*X[c] 
            nuevoVal = (B[f] - nuevo)/A[f,f] #Calculo del nuevo valor X(k+1)
            diferenciaErr[f] = np.abs(X[f] - nuevoVal) #Calculo la diferencia entre el valor anterior de X y el recien caculado
            Xi[f] = nuevoVal
        
        X = Xi
        error = np.max(diferenciaErr) #Obtengo el error de la iteracion k
        print("X = {}\nError = {}".format(X, error))
    
    if error == precision or error < precision:
        print("\nEl valor final de X con una precision de {}, se dio en la iteracion {}".format(precision, k))
        print("X = {}".format(X))
        print("El error obtenido es de: {}".format(error))
    elif k == iteraTot:
        print("\nEl valor final de X obtenido con {} iteraciones".format(k))
        print("X = {}".format(X))
        print("El error obtenido es de: {}".format(error))


#============Metodo de Gauss-Seidel============
def GaussSeidel(A,B,X, iteraTot, precision):
    k = 0 #Iterador
    error = 2 * precision #La cantidad de iteraciones que se haran, dependera de la aproximacion que el error tenga a la precision
    tamanio = np.shape(A) #Obtengo filas y columnas de la matriz A
    filas = tamanio[0]
    columnas = tamanio[1]
    diferenciaErr = np.zeros(filas, dtype=float) #Creo un arreglo de 0s donde guardare los errores calculados en cada operacion

    while error > precision and k < iteraTot:
        k+=1
        print("\nIteracion {}:".format(k))
        for f in range(filas): #iterador de filas
            suma = 0
            for c in range(columnas): #Iterador de columnas
                if(f!=c):
                    suma = suma + A[f,c] * X[c]
            
            nuevoVal = (B[f] - suma) / A[f,f]
            diferenciaErr[f] = np.abs(X[f] - nuevoVal)
            X[f] = nuevoVal #Se cambia el valor de la martiz X(k) por X(k+1)
        
        error = np.max(diferenciaErr)
        print("X = {}\nError = {}".format(X, error))
    
    if error == precision or error < precision:
        print("\nEl valor final de X con una precision de {} se da en la ieracion {}".format(precision, k))
        print("X = {}".format(X))
        print("El error obtenido es de: {}".format(error))
    elif k == iteraTot:
        print("\nEl valor final de X con un total de {} iteraciones maximas.".format(k))
        print("X = {}".format(X))
        print("El error obtenido es de: {}".format(error))

#============Metodo de SobreRelajacion (SOR)============
def Sor(A,B,X,omega, iteraTot, precision):
    k = 0 #Iterador
    error = 2 * precision
    tamanio = np.shape(A)
    filas = tamanio[0]
    columnas = tamanio[1]
    difereciaErr = np.zeros(filas, dtype=float) #Matriz para el calculo del error
    Xi = np.zeros(filas) #Matriz de ceros donde se guardaran los valores anteriores

    while error > precision and k < iteraTot:
        k+=1 
        print("\nIteracion {}:".format(k))
        Xi = X #Igualo la matriz de reserva con la original para usar el valor x(k) que necesito para la ecuacion
        for f in range(filas): #Iterador de filas
            suma = 0
            for c in range(columnas): #Iterador de columnas
                if(f!=c):
                    suma = suma + A[f,c] * X[c]
            nuevoVal = omega * ((B[f]-suma)/A[f,f]) + (1 - omega) * Xi[f] #Nuevo valor X(k+1)
            difereciaErr[f] = np.abs(X[f] - nuevoVal) #Ingreso en el arreglo la diferencia entre el valor anterior y el nuevo
            X[f] = nuevoVal
        
        error = np.max(difereciaErr) #Obtengo el error maximo
        print("X = {}\nError = {}".format(X, error))
    
    if error == precision or error < precision:
        print("\nEl valor final de X con una precision de {} se da en la ieracion {}".format(precision, k))
        print("X = {}".format(X))
        print("El error obtenido es de: {}".format(error))
    elif k == iteraTot:
        print("\nEl valor final de X con un total de {} iteraciones maximas.".format(k))
        print("X = {}".format(X))
        print("El error obtenido es de: {}".format(error))
                


print("\n============Metodo de Jacobi============\n")
jacobi(A,B,X, 30, 0.001)

print("\n============Metodo de Gauss-Seidel============\n")
GaussSeidel(A,B,X, 30, 0.001)


A = np.array([[2,-1,0],[1,6,-2],[4,-3,8]])
B = np.array([2,-4,5])
X = np.zeros(3)

print("\n============Metodo de SOR============\n")
Sor(A,B,X, 0.50, 30, 0.001)