import numpy as np
import os 
import sys

os.system("cls")
#Header
def header():
    print("****************************************")
    print("****************************************")
    print("******  Cálculo de Cadenas de     ******")
    print("******           Markov           ******")
    print("****************************************")
    print("****************************************\n\n")
#Crear Matriz
def crear_matriz():
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
    return matriz
#Imprimir Matriz
def imprimir_matriz():
    print("La Matriz de Trancisión es: ")
    for estado in matriz:
            print("[", end=" ")
            for elemento in estado:
                print("{:8.2f}".format(elemento), end=" ")
            print("]")
#Opciones de Menu
def menu():
    print()
    print("1. Probabilidad: Paso de Primera Vez\n")
    print("2. Estados Recurrentes y Transitorios\n")
    print("3. Probabilidades de Absorción\n")
    print("4. Salir del Programa")
#Primera Vez 
def op_1():
    periodos = int(input("¿En cuántos periodos de tiempo quieres saber la probabilidad?: "))
    print()
    EstadoInicial = int(input("¿Desde qué estado te gustaría iniciar?: "))
    print()
    EstadoFinal = int(input("¿A cuál es el estado al que te gustaría llegar?: "))
    print()

    matrizpot = np.linalg.matrix_power(matriz, periodos)
    print(f"Matriz elevada a la {periodos}-ésima potencia:")
    for fila in matrizpot:
        print("[", end=" ")
        for elemento in fila:
            print(" {:10.2f} ".format(elemento), end="")
        print("]")

    print()

    # Definimos la función para calcular la probabilidad de primer paso
    def P_first(m):
        if m == 0:
            return 0
        if m == 1:
            return matriz[EstadoInicial][EstadoFinal]
        return sum([P_first(m-k)*np.linalg.matrix_power(matriz, k)[EstadoFinal][EstadoFinal] for k in range(1, m)]) * matriz[EstadoInicial][EstadoFinal]

    # Calculamos la probabilidad de primer paso directamente
    P_first_direct = matrizpot[EstadoInicial, EstadoFinal]
    P_first_prob = P_first(periodos)

    # Calculamos la suma de las probabilidades de primer paso anteriores
    sum_P_first = sum([P_first(m) * np.linalg.matrix_power(matrizpot, periodos-m)[EstadoFinal][EstadoFinal] for m in range(1, periodos)])

    # Calculamos la probabilidad de primer paso utilizando la fórmula de renovación
    P_first = P_first_direct - sum_P_first

    print("La probabilidad de primer paso de", EstadoInicial, "a", EstadoFinal, "en", periodos, "pasos es:", P_first)

    
    seguir()
#Estados Recurrentes
def op_2():
    #EstadosRecurrentes

    def identificar_estados_recurrentes_transitorios(matriz_transicion):
        matriz_transicion = np.matrix(matriz)
        num_estados = matriz_transicion.shape[0]
        estados_recurrentes = []
        estados_transitorios = []

        # Identificar las clases de estados
        visitados = np.zeros(num_estados, dtype=bool)

        def dfs(estado):
            visitados[estado] = True
            for estado_siguiente in range(num_estados):
                if matriz_transicion[estado, estado_siguiente] > 0 and not visitados[estado_siguiente]:
                    dfs(estado_siguiente)

        for estado in range(num_estados):
            if not visitados[estado]:
                dfs(estado)
                if np.sum(visitados) == num_estados:
                    estados_recurrentes.extend(np.where(visitados)[0])
                else:
                    estados_transitorios.extend(np.where(visitados)[0])

        # Determinar estados recurrentes
        estados_recurrentes = list(set(estados_recurrentes))
        estados_transitorios = list(set(estados_transitorios))

        # Identificar estados transitorios
        todos_estados = set(range(num_estados))
        estados_transitorios = list(todos_estados - set(estados_recurrentes))

        return estados_recurrentes, estados_transitorios
    estados_recurrentes, estados_transitorios = identificar_estados_recurrentes_transitorios(matriz)

    print("Estados recurrentes:", estados_recurrentes)
    print("Estados transitorios:", estados_transitorios)

    seguir()
#Probabilidades de Absorcion
def op_3():
    #ProbabilidadesDeAbsorcion
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

    seguir()
#Opcion de Salir
def seguir():
    print("Deseas elegir otra opcion?")
    print("1. Si")
    print("2. No")
    respuesta = int(input("Respuesta: "))
    os.system("cls")
    if respuesta == 2 :
        os.system("cls")
        while True:
            # Esperar una entrada del usuario
            user_input = input("Presiona Enter para salir del programa")
    
            # Verificar si la entrada es una cadena vacía
            if user_input == "":
                # Si la entrada es vacía, salir del programa
                os.system("cls")
                sys.exit()
    # else:

header()
Estados = int(input("Indica el número de estados : "))
matriz = crear_matriz()

#CicloMenu
while True:
    imprimir_matriz()
    print("\n ¿Con esta matriz, que deseas conocer?")
    menu()
    print()
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        op_1()
    elif opcion == 2:
        op_2()
    elif opcion == 3:
        op_3()
    elif opcion == 4:
        os.system("cls")
        sys.exit()



