# Escribe un programa con una matriz 3D con listas anidadas para almacenar los datos.
import random
temperaturas = [[[0 for _ in range(24)] for _ in range(4)] for _ in range(3)]

# Llenar la matriz con datos de temperatura randoms o aleatorios.
# Se usan bucles anidados para recorrer cada posición y asignar un valor aleatorio.
for ciudad in range(3):
    for semana in range(4):
        for hora in range(24):
# Se genera una temperatura aleatoria entre 20°C y 35°C.
            temperaturas[ciudad][semana][hora] = random.randint(20, 35)

#Calcular y mostrar el promedio de temperatura para cada ciudad y semana.
print("Promedio de temperatura por ciudad y semana:")

# Bucle principal sobre cada una de las 3 ciudades.
for i, datos_ciudad in enumerate(temperaturas):
    print(f"\n--- Ciudad {i+1} ---")

    # Bucle anidado sobre las 4 semanas de cada ciudad.
    for j, datos_semana in enumerate(datos_ciudad):
        total_semana = sum(datos_semana)
        cantidad_horas = len(datos_semana)
        if cantidad_horas > 5:
            promedio = total_semana / cantidad_horas
            print(f"  --Semana {j+1}: {promedio:.2f}°C")
        else:
            print(f"  Dia {j+1}: No hay datos.")