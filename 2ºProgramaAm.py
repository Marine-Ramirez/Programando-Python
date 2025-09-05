# Escribe un programa que incluya una matriz bidimensional puede ser de 3x3 con valores numericos.
matriz = [
    [30, 10, 20],
    [90, 80, 70],
    [60, 40, 50]
]

#Implementamos el algoritmo QuickSort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]    
    return quick_sort(left) + middle + quick_sort(right)

# Función para ordenar una fila específica de la matriz

def ordenar_fila_matriz(matriz, fila_a_ordenar):
    if fila_a_ordenar < 0 or fila_a_ordenar >= len(matriz):
        print("Error: El número de fila está fuera de los límites de la matriz.")
        return
    
# Ordenamos la fila usando la función quick_sort
    matriz[fila_a_ordenar] = quick_sort(matriz[fila_a_ordenar])

# Paso 4: Mostramos la matriz original y la matriz con la fila ordenada

print("Matriz Original:")
for fila in matriz:
    print(fila)

# Definimos la fila que queremos ordenar (usando indexación desde 0)
# Por ejemplo, ordenaremos la segunda fila (índice 1)
fila_a_ordenar = 1 
ordenar_fila_matriz(matriz, fila_a_ordenar)

print("\nMatriz con la fila", fila_a_ordenar, "ordenada:")
for fila in matriz:
    print(fila)

