# ==========================================
#               EJERCICIO 1
# ==========================================

def imprimir_hola_mundo():
    ## Esta función imprime "Hola Mundo :D!" en la consola.
    print("Hola Mundo :D!")    
imprimir_hola_mundo()

# ==========================================
#               EJERCICIO 2
# ==========================================

def saludar_usuario(nombre):
    ## Esta función saluda al usuario por su nombre.
    print(f"Hola {nombre}!")
saludar_usuario("Emanuel")

# ==========================================
#               EJERCICIO 3
# ==========================================

def informacion_personal(nombre, apellido, edad, residencia):
    ## Esta función imprime la información personal del usuario.
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
    
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# ==========================================
#               EJERCICIO 4
# ==========================================

import math
def calcular_area_circulo(radio):
    ## Calcula el área de un círculo dado su radio.
    area = math.pi * radio ** 2
    return area
def calcular_perimetro_circulo(radio):
    ## Calcula el perímetro de un círculo dado su radio.
    perimetro = 2 * math.pi * radio
    return perimetro

radio = float(input("Ingrese el radio del círculo: "))
print(f"El área del círculo es: {calcular_area_circulo(radio)}")
print(f"El perímetro del círculo es: {calcular_perimetro_circulo(radio)}")

# ==========================================
#               EJERCICIO 5
# ==========================================

def segundos_a_horas(segundos):
    ## Esta función convierte segundos a horas.
    horas = segundos // 3600
    return horas
segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"{segundos} segundos son {segundos_a_horas(segundos)} horas.")

# ==========================================
#               EJERCICIO 6
# ==========================================

def tabla_multiplicar(numero):
    ## Imprime la tabla de multiplicar del número dado
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
num = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(num)

# ==========================================
#               EJERCICIO 7
# ==========================================

def operaciones_basicas(a, b):
    ## Realiza las operaciones básicas entre dos números y devuelve los resultados.
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(num1, num2)
print(f"Suma: {resultados[0]}\nResta: {resultados[1]}\nMultiplicación: {resultados[2]}\nDivisión: {resultados[3]}")