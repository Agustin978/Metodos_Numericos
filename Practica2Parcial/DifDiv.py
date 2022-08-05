import numpy as np

x = np.array([4.,-4.,7.,6.,2.])
y = np.array([278.,-242.,1430.,980.,40.])

def DifDiv(x,y):
    n = len(x) #Longitud del arreglo de datos
    D = np.zeros(n) #Arreglo donde se guardaran las diferencias divididas
    c = 0 #Variable para manejarme en el denominador
    D[0] = y[0]
    for i in range(1,n,1):
        c -= 1
        print("\nDiferencias divididas en iteracion {}:\n".format(i))
        for j in range(n,i,-1):
            j-=1
            y[j] = round((y[j]-y[j-1])/(x[j]-x[j+c]),5)
            print(y[j])
        D[i] = y[i]
    return D
Dif_div = DifDiv(x,y)
print("Diferencia Dividida:\n{}".format(Dif_div))
