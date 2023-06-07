Estados = int(input("Indica el número de estados: "))

def crear_matriz():
    matriz = []

    matriz_valida = False
    while not matriz_valida:
        matriz = []
        for i in range(Estados):
            fila = []
            suma_fila = 0.0
            for j in range(Estados):
                valor = float(input("Dame el valor del estado {}, {}: ".format(i, j)))
                fila.append(valor)
                suma_fila += valor
            matriz.append(fila)
            if suma_fila != 1.0:
                print(f"La suma de la fila {i+1} no es igual a 1. Por favor, ingresa los valores nuevamente.")
                break
        else:
            matriz_valida = True

    print()
    print("La Matriz de Trancisión es: ")
    for estado in matriz:
            print("[", end=" ")
            for elemento in estado:
                print("{:8.2f}".format(elemento), end=" ")
            print("]")

crear_matriz()
