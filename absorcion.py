import numpy as np

def probabilidades_absorcion(matriz):
    n = matriz.shape[0]
    identidad = np.eye(n)

    # Verificar si hay estados absorbentes
    if not np.any(np.diag(matriz) == 1):
        raise ValueError("La matriz no tiene estados absorbentes.")

    # Obtener la matriz Q
    estados_absorbentes = np.where(np.diag(matriz) == 1)[0]
    estados_no_absorbentes = np.where(np.diag(matriz) != 1)[0]

    Q = matriz[estados_no_absorbentes][:, estados_no_absorbentes]
    R = matriz[estados_no_absorbentes][:, estados_absorbentes]

    N = np.linalg.inv(identidad - Q)
    B = np.dot(N, R)
    probabilidades = B.flatten()
    return probabilidades

def tiene_estados_absorcion(matriz):
    estados_absorcion = np.where(np.diag(matriz) == 1)[0]
    return len(estados_absorcion) > 0

# Ingresar el número de estados
Estados = int(input("Indica el número de estados: "))

matriz_valida = False
while not matriz_valida:
    matriz = []
    for i in range(Estados):
        fila = []
        suma_fila = 0.0
        for j in range(Estados):
            valor = float(input("Dame el valor del estado {}, {}: ".format(i , j)))
            fila.append(valor)
            suma_fila += valor
        matriz.append(fila)
        if suma_fila != 1.0:
            print(f"La suma de la fila {i+1} no es igual a 1. Por favor, ingresa los valores nuevamente.")
            break
    else:
        matriz_valida = True

matriz_array = np.array(matriz)
print("\nMatriz de transición sin Numpy:")
print(matriz)

print("\nMatriz de transición con Numpy:")
print(matriz_array)

if tiene_estados_absorcion(matriz_array):
    try:
        probabilidades = probabilidades_absorcion(matriz_array)
        print("\nProbabilidades de absorción:")
        for i, probabilidad in enumerate(probabilidades):
            print(f"Estado {i+1}: {probabilidad}")
    except ValueError as error:
        print(f"\nError: {str(error)}")
else:
    print("\nLa matriz no tiene estados de absorción.")
