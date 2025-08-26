# ============================
# Programa 2: Ordenar una fila de la Matriz
# ============================

def bubble_sort(lista):
    """
    Ordena una lista usando Bubble Sort.
    :param lista: Lista de números.
    :return: Lista ordenada.
    """
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def ordenar_fila_matriz(matriz, fila):
    """
    Ordena una fila específica de una matriz.
    :param matriz: Lista de listas (matriz).
    :param fila: Índice de la fila a ordenar.
    :return: Matriz con la fila ordenada.
    """
    matriz[fila] = bubble_sort(matriz[fila])
    return matriz


# Definimos una matriz 3x3
matriz = [
    [10, 2, 7],
    [5, 12, 1],
    [8, 3, 9]
]

# Fila a ordenar (0 primera fila, 1 segunda, etc.)
fila_a_ordenar = 1

print("=== MATRIZ ORIGINAL ===")
for fila in matriz:
    print(fila)

# Ordenamos la fila seleccionada
matriz_ordenada = ordenar_fila_matriz(matriz, fila_a_ordenar)

print("\n=== MATRIZ CON LA FILA ORDENADA ===")
for fila in matriz_ordenada:
    print(fila)
