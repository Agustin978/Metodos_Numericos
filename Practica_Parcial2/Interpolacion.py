import numpy as np
import sympy as sym
import decimal as dec

def DifDiv(x, y): #Recibo dos arreglos con los elementos de la tabla
    n = len(x) #Cantidad de datos o puntos que obtengo de la tabla
    Dif = np.zeros(n) #Arreglo de longitud n donde se guardaran las diferencias divididas
    c = 0 #Variable que uso en la X del denominador
    Dif[0] = y[0] #Inicio el valor de las diferencias divididas con el primer elemento del arreglo de y
    for i in range(1,n,1):
        c -= 1
        #print("Valor de c {}".format(c))
        print("\nDiferencia dividida de la iteracion {}".format(i))
        for j in range(n,i,-1):
            j -= 1 #Como los arreglos se recorren de atras a adelante
            #print("Valor de j {} / Valor de y1 {} y2 {} / Valor en X1 {} X2 {}".format(j, y[j], y[j-1], x[j], x[j+c]))
            y[j] = round((y[j] - y[j-1]) / ( x[j] - x[j+c] ) , 5)
            print(y[j])
        Dif[i] = y[i]
    
    return Dif

x = np.array([4.,-4.,7.,6.,2.])
y = np.array([278.,-242.,1430.,980.,40.])

D = DifDiv(x,y)
print(D)