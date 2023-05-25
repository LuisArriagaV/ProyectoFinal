import numpy as np

def suma(matriz, x, y, n):
    P_n = np.linalg.matrix_power(matriz, n)
    PrimeraProba = matriz[x][y]
    sumaProbas = 0

    for m in range(1, n):
        sumaProbas += sum(suma(matriz, x, y, m) * np.linalg.matrix_power(matriz, n - m)[y][y] for k in range(1, n))

    PrimeraProba = PrimeraProba - sumaProbas

    return PrimeraProba

Estados = int(input("Indica el número de estados: "))

# Generación de la matriz
matriz = []
for i in range(Estados):
    matriz.append([])
    for j in range(Estados):
        valor = float(input("Dame el valor del estado {}, {}: ".format(i, j)))
        matriz[i].append(valor)

x = int(input("Estado Inicial: "))
y = int(input("Estado Final: "))
n = Estados

primer = suma(matriz, x, y, n)

print("La suma es: ")
print(primer)