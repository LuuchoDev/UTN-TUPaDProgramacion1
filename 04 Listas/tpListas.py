# ==========================================
#               EJERCICIO 1
# ==========================================

notas = [10, 8, 7, 6, 10, 4, 8, 7, 6, 5]
print(f"Notas de los estudiantes: {notas}")
    
## Calcular y mostrar el promedio de las notas
promedio = sum(notas) / len(notas)
print(f"Promedio de las notas: {promedio}")

## Indicar la nota más alta y la más baja
print(f"La nota mas alta es: {max(notas)}")
print(f"La nota mas baja es: {min(notas)}")

# ==========================================
#               EJERCICIO 2
# ==========================================

## Crea una lista vacía para almacenar productos
productos = []
print("Ingrese los productos que desea agregar: ")
## Solicita al usuario que ingrese 5 productos
for i in range(5):
    producto = input(f"Producto {i+1}: ")
    productos.append(producto)

## Muestra la lista en orden alfabético
productos_ordenados = sorted(productos)
print("Lista de productos en orden alfabético:")
for p in productos_ordenados:
    print(f"- {p}")

## Consulta al usuario si desea eliminar un producto
EliminarSioNo = input("¿Desea eliminar algún producto de la lista? (s/n): ")
if EliminarSioNo in 'sS':
    producto_a_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
    ## verifica si el producto está en la lista antes de eliminarlo
    if producto_a_eliminar in productos:
        productos.remove(producto_a_eliminar)
        print(f"Producto '{producto_a_eliminar}' eliminado.")
        ## Muestra la lista actualizada luego de eliminar el producto
        print("Lista actualizada de productos:")
        for p in productos:
            print(f"- {p}")
    else:
        print(f"Producto '{producto_a_eliminar}' no encontrado en la lista.")
else:
    ## Muestra la lista actualizada
    print("Lista actualizada de productos:")
    for p in productos:
        print(f"- {p}")
        
# ==========================================
#               EJERCICIO 3
# ==========================================

import random
numerosRandom = []
## Genera 15 números aleatorios entre 1 y 100
for i in range(15):
    numerosRandom.append(random.randint(1, 100))

## Crea una lista con los numeros pares y otra con los impares
numerosPares = []
numerosImpares = []

for num in numerosRandom:
    if num % 2 == 0:
        numerosPares.append(num)
    else:
        numerosImpares.append(num)

## Muestra la lista de pares e impares
print(f"Números generados: {numerosRandom}")
print(f"Números pares: {numerosPares} (cantidad: {len(numerosPares)})")
print(f"Números impares: {numerosImpares} (cantidad: {len(numerosImpares)})")

# ==========================================
#               EJERCICIO 4
# ==========================================

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_sin_repetidos = []

## Crea una nueva lista sin elementos repetidos
for num in datos:
    if num not in datos_sin_repetidos:
        datos_sin_repetidos.append(num)
    else:
        continue

print(datos_sin_repetidos)

# ==========================================
#               EJERCICIO 5
# ==========================================

## Lista de alumnos
alumnos = ["Ana", "Luis", "Carlos", "Marta", "Lucía", "Jorge", "Sofía", "Diego"]
print(alumnos)

## Consulta al usuario si desea agregar un nuevo alumno o eliminar uno existente.
Agregar_O_Eliminar = input("¿Desea agregar un nuevo alumno (a) o eliminar uno existente (e)? (a/e): ")
if Agregar_O_Eliminar in 'aA':
    ## Solicita el nombre del nuevo alumno
    nuevo_alumno = input("Ingrese el nombre del nuevo alumno: ")
    alumnos.append(nuevo_alumno)
    print(f"Alumno '{nuevo_alumno}' agregado.")
elif Agregar_O_Eliminar in 'eE':
    ## Solicita el nombre del alumno a eliminar
    alumno_a_eliminar = input("Ingrese el nombre del alumno que desea eliminar: ")
    ## Verifica si el alumno está en la lista antes de eliminarlo
    if alumno_a_eliminar in alumnos:
        alumnos.remove(alumno_a_eliminar)
        print(f"Alumno '{alumno_a_eliminar}' eliminado.")
    else:
        print(f"Alumno '{alumno_a_eliminar}' no encontrado en la lista.")

print(f"La lista actualizada es: {alumnos}")

# ==========================================
#               EJERCICIO 6
# ==========================================

numeros = [1, 2, 3, 4, 5, 6, 7]
## Muestra la lista original
print(f"Lista original: {numeros}")
## Rota la lista a la derecha una vez
numeros = [numeros[-1]] + numeros[:-1]
print(f"Lista rotada: {numeros}")

# ==========================================
#               EJERCICIO 7
# ==========================================

temperaturas = [
    [10, 20],
    [12, 22],
    [8, 18],
    [11, 21],
    [9, 19],
    [13, 23],
    [7, 17]
]
## calcular el promedio de las minimas y maximas
minimas = [fila[0] for fila in temperaturas]
maximas = [fila[1] for fila in temperaturas]

promedio_minimas = sum(minimas) / len(minimas)
promedio_maximas = sum(maximas) / len(maximas)
print(f'Promedio de temperaturas mínimas: {promedio_minimas}')
print(f'Promedio de temperaturas máximas: {promedio_maximas}')

# ==========================================
#               EJERCICIO 8
# ==========================================

notas = [
    [8, 7, 9],   # Estudiante 1
    [6, 5, 7],   # Estudiante 2
    [9, 8, 10],  # Estudiante 3
    [7, 6, 8],   # Estudiante 4
    [10, 9, 9]   # Estudiante 5
]

## Calcula y muestra el promedio de cada estudiante
for i in range(len(notas)):
    promedio = sum(notas[i]) / len(notas[i])
    print(f"El promedio del estudiante {i+1} es: {promedio}.")
    
## Calcula y muestra el promedio de cada materia
for j in range(3):
    suma = 0
    for i in range(len(notas)):
        suma += notas[i][j]
    promedio = suma / len(notas)
    print(f"El promedio de la materia {j+1} es: {promedio:.2f}.")
    
# ==========================================
#               EJERCICIO 9
# ==========================================

# Inicializa el tablero 3x3 con guiones
tablero = []
for i in range(3):
    fila = []
    for j in range(3):
        fila.append("-")
    tablero.append(fila)

## Muestra el tablero inicial
for fila in tablero:
    for celda in fila:
        print(celda, end=" ")
    print()
    
## Variables para controlar el juego
jugador = "x"
jugadas = 0

while jugadas < 9:
    print(f"\nTurno del jugador '{jugador}'")
    fila = int(input(f"Jugador '{jugador}', ingrese la fila (0-2): "))
    columna = int(input(f"Jugador '{jugador}', ingrese la columna (0-2): "))
    
    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Coordenadas inválidas. Intente de nuevo.")
        continue # Salta a la siguiente iteración del bucle
    
    if tablero[fila][columna] != "-":
        print("La celda ya está ocupada. Intente de nuevo.")
        continue # Salta a la siguiente iteración del bucle

    # Realiza la jugada
    tablero[fila][columna] = jugador
    jugadas += 1
    
    # Cambia de jugador
    jugador = "o" if jugador == "x" else "x"

    # Muestra el tablero
    for fila in tablero:
        for celda in fila:
            print(celda, end=" ")
        print()

# ==========================================
#               EJERCICIO 10
# ==========================================

