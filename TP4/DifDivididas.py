import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

x = np.array([4, -4, 7, 6, 2])
y = np.array([278, -242, 1430, 980, 40])
#===========Metodo de Newton (Diferencias divididas)===========
def Dif_Divididas(x, y, len(x)):
    n = len(x)
    titulo = ['   i   ', '   Xi   ','   fi   ']
    k = np.arange(0, n, 1)
    tabla = np.concatenate(([k], [x], [y]), axis=1)
    tabla = np.transpose(tabla)

    difDiv = np.zeros(shape=(n,n), dtype=float)
    tabla = np.concatenate((tabla, difDiv), axis=1)

    [filas, columnas] = np.shape(tabla)
    diagonal = n-1
    j = len(y)

    while j < columnas:
        titulo.append('F[{}]'.format(str(j-2)))

        i = 0
        paso = j-2
        while i < diagonal:
            denominador = (x[i+paso]-x[i])
            numerador = tabla[i+1,j-1] - tabla[i, j-1]
            tabla[i,j] = numerador/denominador
            i+=1
        diagonal = diagonal - 1
        j+=1
    
    #Polinomio con diferencias divididas
    dDividida = tabla[0,j:]
    n = len(difDiv)

    #Grafica de la funcion
    t = sym.Symbol('x')
    polinomio = y[0]

    for j in range(1,n,1):
        factor = dDividida[j-1]
        termino = 1
        for k in range(0,j,1):
            termino = termino*(t - x[k])
        polinomio = polinomio + termino*factor

    poliSimple = sym.expand(polinomio)

    px = sym.lambdify(t, poliSimple)


