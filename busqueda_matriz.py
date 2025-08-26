# ============================
# Programa 1: Búsqueda en Matriz 3x3
# ============================

def buscar_en_matriz(matriz, valor):
    """
    Busca un valor en una matriz bidimensional.
    :param matriz: Lista de listas (matriz).
    :param valor: Valor a buscar.
    :return: Tupla (fila, columna) si se encuentra, None si no.
    """
    for i, fila in enumerate(matriz):
        for j, elemento in enumerate(fila):
            if elemento == valor:
                return i, j
    return None


# Definimos una matriz 3x3
matriz = [
    [12, 7, 5],
    [9, 15, 3],
    [4, 8, 11]
]

# Valor a buscar
valor_buscado = 15

print("=== MATRIZ ===")
for fila in matriz:
    print(fila)

# Llamamos a la función de búsqueda
posicion = buscar_en_matriz(matriz, valor_buscado)

# Resultado
if posicion:
    print(f"\n✅ Valor {valor_buscado} encontrado en la posición (fila={posicion[0]}, columna={posicion[1]}).")
else:
    print(f"\n❌ Valor {valor_buscado} NO encontrado en la matriz.")
