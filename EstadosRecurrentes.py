def identificar_estados_transitorios_recurrentes(matriz_transicion):
    # Obtener el tamaño de la matriz
    n = len(matriz_transicion)
    
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
                    if matriz_transicion[estado_actual][j] > 0 and not visitados[j]:
                        # Marcar el estado j como visitado
                        visitados[j] = True
                        
                        # Agregar el estado j a la lista de estados alcanzables
                        estados_alcanzables.append(j)
            
            # Si el estado actual es alcanzable desde sí mismo, es un estado recurrente; de lo contrario, es un estado transitorio
            if matriz_transicion[estado_actual][estado_actual] > 0:
                print(f"El estado {i} es recurrente.")
            else:
                print(f"El estado {i} es transitorio.")

# Ejemplo de uso
matriz_transicion = [
    [0.5, 0.5, 0.0],
    [0.0, 0.5, 0.5],
    [0.0, 0.0, 1.0]
]

identificar_estados_transitorios_recurrentes(matriz_transicion)