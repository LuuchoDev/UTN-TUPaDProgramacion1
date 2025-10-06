## Ejercicio 1
def imprimir_hola_mundo():
    ## Esta función imprime "Hola Mundo :D!" en la consola.
    print("Hola Mundo :D!")    
imprimir_hola_mundo()

## Ejercicio 2
def saludar_usuario(nombre):
    ## Esta función saluda al usuario por su nombre.
    print(f"Hola {nombre}!")
saludar_usuario("Emanuel")

## Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    ## Esta función imprime la información personal del usuario.
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
    
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

## Ejercicio 4
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

## Ejercicio 5
def segundos_a_horas(segundos):
    ## Esta función convierte segundos a horas.
    horas = segundos // 3600
    return horas
segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"{segundos} segundos son {segundos_a_horas(segundos)} horas.")

## Ejercicio 6
