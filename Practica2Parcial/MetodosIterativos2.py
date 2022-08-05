import numpy as np

#A = np.loadtxt('TP3/A.txt',delimiter=',')
#B = np.loadtxt('TP3/b.txt',delimiter=',')
#X = np.loadtxt('TP3/X.txt',delimiter=',')

A = np.array([[6,-2,1],[-2,7,2],[1,2,-5]])
B = np.array([4,1,-4.5])
X = np.zeros(3)

def Jacobi(A, B, X, iteraMax, eps):
    k = 0
    tamanio = np.shape(A)
    filas = tamanio[0]
    columnas = tamanio[1]
    error = 2 * eps
    dif = np.zeros(filas, dtype=float)
    Xi = np.zeros(filas)
    while error > eps and k < iteraMax:
        k+=1
        print("\nIteracion {}:".format(k))
        for f in range(filas):
            suma = 0
            for c in range(columnas):
                if(f!=c):
                    suma += A[f,c] * X[c]
            Xi[f] = (B[f] - suma) / A[f,f]
            dif[f] = np.abs(X[f] - Xi[f])
            X[f] = Xi[f]
        error = np.max(dif)
        print("X = {}\nError: {}".format(X, error))
    
    if error == eps or error < eps:
        print("\nEl valor de X obtenido con una precision de {} es:".format(eps))
        print("X = {}\nError: {}".format(X, eps))
    elif k == iteraMax:
        print("\nEl valor de X obtenido con una cantidad maxima de {} iteraciones es:".format(k))
        print("X = {}\nError: {}".format(X, error))

def Gauss_Seidel(A,B,X,iteMax,precision):
    k=0
    error = 2*precision
    tamanio = np.shape(A)
    filas = tamanio[0]
    columnas = tamanio[1]
    diff = np.ones(filas, dtype=float)
    while error > precision and k < iteMax:
        k += 1
        print("\nIteracion {}:".format(k))
        for f in range(filas):
            suma = 0
            for c in range(columnas):
                if f!=c:
                    suma += A[f,c]*X[c]
            nuevo = (B[f] - suma)/A[f,f]
            diff[f] = np.abs(nuevo - X[f])
            X[f] = nuevo
        error = np.max(diff)
        print("X = {}\nError: {}".format(X, error))
    
    if error == precision or error < precision:
        print("\nEl valor de X obtenido con una precision de {} es:".format(precision))
        print("X = {}\nError: {}".format(X, error))
    elif k == iteMax:
        print("\nEl valor de X obtenido con una cantidad de {} iteraciones es:".format(iteMax))
        print("X = {}\nError: {}".format(X, error))


def Sor(A,B,X,omega,iteMax,precision):
    k = 0
    tamanio = np.shape(A)
    filas = tamanio[0]
    columnas = tamanio[1]
    diff = np.zeros(filas, dtype=float)
    error = 2*precision
    while error > precision or k < iteMax:
        k+=1
        print("\nIteracion {}:".format(k))
        for f in range(filas):
            suma = 0
            for c in range(columnas):
                if f!=c:
                    suma += A[f,c] * X[c]
            nuevo = (1 - omega) * X[f] + (B[f] - suma)*(omega/A[f,f])
            diff[f] = np.abs(nuevo - X[f])
            X[f] = nuevo
        error = np.max(diff)
        print("X = {}\nError: {}".format(X, error))

    if error == precision or error < precision:
        print("\nEl valor de X obtenido con una precision de {} es:".format(precision))
        print("X = {}\nError: {}\nObtenido en la iteracion: {}".format(X,error,k))
    elif k == iteMax:
        print("\nEl valor de X obtenido con un total de {} iteraciones es:".format(iteMax))
        print("X = {}\nError: {}".format(X,error))

#print("\n===========Metodo de Jacobi===========\n")
#Jacobi(A,B,X,3,0.001)

#print("\n===========Metodo de Gauss-Seidel===========\n")
#Gauss_Seidel(A,B,X,4,0.00001)

print("\n===========Metodo de SOR===========\n")
Sor(A,B,X,0.5,4,0.00001)           