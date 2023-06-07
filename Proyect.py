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
    #PrimeraVez
    periodos = int(input("¿En cuantos periodos de tiempo queres saber la probabilidad?:  ")) 
    print()
    EstadoInicial = int(input("¿Desde que estado te gustaria iniciar?: "))
    print()
    EstadoFinal = int(input("¿A cual es el estado que te gustaria llegar final?: "))
    print()

    matrizpot = np.linalg.matrix_power(matriz, periodos)
    print(f"Matriz a la {periodos} potencia.")
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
        return sum([P_first(m-k)*np.linalg.matrix_power(matriz, k)[EstadoFinal][EstadoFinal] for k in range(1, m)])*matriz[EstadoInicial][EstadoFinal]

    # Calculamos la probabilidad de primer paso directamente
    P_first_direct = matrizpot[EstadoInicial, EstadoFinal]
    P_first(periodos)


    #Calculamos la suma de las probabilidades de primer paso anteriores
    sum_P_first = sum([P_first(m)*np.linalg.matrix_power(matrizpot, periodos-m)[EstadoFinal][EstadoFinal] for m in range(1,periodos)])

    # Calculamos la probabilidad de primer paso utilizando la fórmula de renovación
    P_first = P_first_direct - sum_P_first


    print("La probabilidad de primer paso de x a y en", periodos, "pasos es:", P_first)

    
    seguir()
#Estados Recurrentes
def op_2():
    #EstadosRecurrentes
    # Obtener el tamaño de la matriz
    n = len(matriz)
    # Crear una lista de estados visitados
    visitados = [False] * n
    # Iterar sobre cada estado de la matriz
    for i in range(n):
        # Si el estado i no ha sido visitado
        if not visitados[i]:
            # Marcar el estado actual como visitado
            visitados[i] = True
            
            # Crear una lista de estados alcanzables desde el estado actual
            estados_alcanzables = [i]
            
            # Iterar hasta que no haya más estados alcanzables desde el estado actual
            while estados_alcanzables:
                # Tomar el primer estado de la lista
                estado_actual = estados_alcanzables.pop(0)
                
                # Iterar sobre los estados de la matriz para verificar si son alcanzables desde el estado actual
                for j in range(n):
                    # Si hay una transición del estado actual al estado j
                    if matriz[estado_actual][j] > 0 and not visitados[j]:
                        # Marcar el estado j como visitado
                        visitados[j] = True
                        
                        # Agregar el estado j a la lista de estados alcanzables
                        estados_alcanzables.append(j)
            
            # Si el estado actual es alcanzable desde sí mismo, es un estado recurrente; de lo contrario, es un estado transitorio
            if matriz[estado_actual][estado_actual] > 0:
                print(f"El estado {i} es recurrente.")
            else:
                print(f"El estado {i} es transitorio.")


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
            user_input = input("Presiona Enter para salir del programa: ")
    
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



