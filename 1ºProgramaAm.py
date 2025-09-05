# Escribe un programa que incluya una matriz bidimensional puede ser de 3x3 con valores numericos.
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Definimos el valor que queremos encontrar.
valor_a_buscar = 90

# Paso 3: Implementar una función para buscar el valor
def buscar_valor_en_matriz(matriz, valor):
    """
    Busca un valor específico en una matriz bidimensional.
    Retorna la posición (fila, columna) si el valor se encuentra, de lo contrario, retorna None.
    """
    for fila_index, fila in enumerate(matriz):
        for col_index, elemento in enumerate(fila):
            if elemento == valor:
                return (fila_index, col_index)
    return None  
posicion = buscar_valor_en_matriz(matriz, valor_a_buscar)
if posicion:
    print(f"El valor {valor_a_buscar} se encontró.")
    print(f"Su posición es: fila {posicion[0]}, columna {posicion[1]}.")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")