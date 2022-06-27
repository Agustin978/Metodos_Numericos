import numpy as np
import sympy as sym
import decimal as dec

def DifDiv(x,f):
    
    n = len(x) ## da el tamaño del vector x
    D = np.zeros(n) ## me da un vector nulo de tamaño n, aca se guardaran las diferencias divididas
    c=0 ## variable q ira en el x denominador
    D[0]=f[0]
    for i in range(1,n,1):
        c=c-1
        print("Diferencia dividida de la iteracion: ", i)
        for j in range(n,i,-1):
            j=j-1
            f[j] =round( (f[j] - f[j-1]) / (x[j] - x[j+c]) , 5 )
            print(f[j])
        D[i]=f[i]
    
    return D

def polinomioInterpolante(xi,fi,D):
    x = sym.Symbol('x')
    n = len(xi)
    polinomio = 0
    print("***** Polinomio *****\n")
    print(polinomio)
    
    for i in range (1,n,1):
        termino = 1
        for j in range (0,i,1):
            termino= termino * (x - xi[j]) ## cada termino de (x-xi) en cada iteracion se van acumulando. todo dentro del for j
        print("\n Termino")
        print(termino)
        polinomio = polinomio + ((termino) * D[i]) ## se va armando el polinomio  
        print("***** Polinomio *****\n")
        print(polinomio)
   
    polinomio = polinomio + D[0]
    print("\n***** Polinomio final *****\n")
    print(polinomio)

xi = np.array([4.,-4.,7.,6.,2.])
fi = np.array([278.,-242.,1430.,980.,40.])


D = DifDiv(xi,fi)

print(D)
#polinomioInterpolante(xi,fi,D)