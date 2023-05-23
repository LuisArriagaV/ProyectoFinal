import numpy as np
import os 
import sys

os.system("cls")

print("******************************************")
print("******************************************")
print("******  Cálculo de Cadenas de       ******")
print("******           Markov             ******")
print("******************************************")
print("******************************************\n\n")


Estados = int(input("Indica el número de estados : "))

#Matrix generation
matriz = []
for i in range(Estados):
    matriz.append([])
    for j in range(Estados):
        valor = float(input("Dame el valor del estado {}, {}:  ".format(i , j)))
        

        matriz[i].append(valor)
        print()

regreso = 1

while regreso == 1: 
    
    print()
    for estado in matriz:
        print("[", end=" ")
        for elemento in estado:
            print("{:8.2f}".format(elemento), end=" ")
        print("]")
    print()

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

    print("¿Deseas conocer otra probabilidad?")
    print("1 = SI \n 2 = NO\n")
    regreso = int(input("Respuesta: "))
    if (regreso == 1):
            os.system("cls")


while True:
    # Esperar una entrada del usuario
    user_input = input("Presiona Enter para salir del programa: ")
    
    # Verificar si la entrada es una cadena vacía
    if user_input == "":
        # Si la entrada es vacía, salir del programa
        os.system("cls")
        sys.exit()
    
    # Si la entrada no es vacía, continuar con el programa
    # ...