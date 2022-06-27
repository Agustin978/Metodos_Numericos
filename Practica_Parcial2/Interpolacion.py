from turtle import color
import numpy as np
import sympy as sym
import decimal as dec
import matplotlib.pyplot as plt 
from scipy.interpolate import CubicSpline

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

#Forma el polinomio interpolante
def PolinomioInterpolante(xi, y, Dif):
    x = sym.Symbol('x') #Un string para completar el polinomio
    n = len(xi) #Cantidad de datos o puntos que obtengo de la tabla
    polinomio = 0
    print("====Polinomio====\n")
    print(polinomio)

    for i in range(1,n,1):
        termino = 1
        for j in range(0,i,1):
            termino = termino * (x - xi[j]) #Cada termino de (x-xi) se acumulan dentro del for de j
        print("\nTermino: {}".format(termino))
        polinomio += ((termino) * Dif[i]) #Armado del polinomio
        print("\n====Polinomio====\n{}".format(polinomio))
    
    polinomio += D[0]
    print("\n====Polinomio Final====\n{}".format(polinomio))
  

x = np.array([4.,-4.,7.,6.,2.])
y = np.array([278.,-242.,1430.,980.,40.])

D = DifDiv(x,y)
print(D)
PolinomioInterpolante(x,y,D)

#Cubic Spline
x = [0.9,1.3,1.9,2.1,2.6,3.0,3.9,4.4,4.7,5.0,6.0,7.0,8.0,9.2,10.5,11.3,11.6,12.0,12.6,13.0,13.3]
y = [1.3,1.5,1.85,2.1,2.6,2.7,2.4,2.15,2.05,2.1,2.25,2.3,2.25,1.95,1.4,0.9,0.7,0.6,0.5,0.4,0.25]

f = CubicSpline(x, y, bc_type="natural")
x_toPlot = np.linspace(0.9, 13.3, 300) #Rango de x, tomando 300 puntos
y_cubic = f(7.3)
print("\nValor de cubic spline en 7.3: {}".format(y_cubic))

plt.figure(figsize=(14, 2)) #Para el tamaño de la grafica 
plt.plot(x,y,":" ,color="b") #Forma y color de la funcion interpolante
plt.plot(x,y,'go') #Puntos de la funcion
plt.title("Interpolacion Cubic_Spline", size=26) #Titulo de la grafica
plt.xlabel('X', size = 25)
plt.ylabel('Y', size = 25)
plt.legend('f', loc = 'upper right')
plt.show()