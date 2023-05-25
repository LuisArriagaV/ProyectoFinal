import numpy as np


def suma(x,y,n):
    m = n-1
    x = EstadoInicial
    y = EstadoFinal

    if m == 0:
        return 0
    
    if m == 1:
        return  np.linalg.matrix_power(matriz,n)[x,y]
    
    return suma

EstadoInicial = 1
EstadoFinal = 5
n=6

Estados = int(input("Indica el número de estados : "))

#Matrix generation
matriz = []
for i in range(Estados):
    matriz.append([])
    for j in range(Estados):
        valor = float(input("Dame el valor del estado {}, {}:  ".format(i , j)))
        

        matriz[i].append(valor)
        print()

print("La suma es : ")
print(suma(EstadoInicial,EstadoFinal,n))