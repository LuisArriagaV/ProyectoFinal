import numpy as np

def P_first_passage(p, x, y, n):
    """
    Calcula la probabilidad de primer paso de x a y en n pasos usando la fórmula de renovación.
    """
    P_n = np.linalg.matrix_power(p, n)  # Matriz de transición a la n
    P_first = P_n[x][y]  # Probabilidad de primer paso directa
    
    for m in range(1, n):
        # Suma de las probabilidades de primer paso anteriores
        sum_P_first = sum(P_first_passage(p, x, y, m) * np.linalg.matrix_power(p, n-m)[y][y] for m in range(1, n))
    
    P_first = P_first - sum_P_first  # Probabilidad de primer paso utilizando la fórmula de renovación
    
    return P_first

# Definir la matriz de transición P
p = np.array([[0.3, 0.5, 0.2],
              [0.1, 0.6, 0.3],
              [0.2, 0.4, 0.4]])

# Definir el estado inicial x
x = 0

# Definir el estado objetivo y
y = 2

# Definir el número de pasos n
n = 5

# Calcular la probabilidad de primer paso utilizando la fórmula de renovación
P_first = P_first_passage(p, x, y, n)

print("La probabilidad de primer paso P_x(T_y =", n, ") es:", P_first)
