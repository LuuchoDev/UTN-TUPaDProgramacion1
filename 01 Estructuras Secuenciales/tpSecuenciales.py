## Ejercicio 1
print("Hola Mundo!")

## Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

## Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su ciudad de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

## Ejercicio 4
import math
radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * radio ** 2
print(f"El área del círculo con radio {radio} es {area}.")

## Ejercicio 5
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos // 3600
print(f"{horas} horas")

## Ejercicio 6

numero = int(input("Ingrese un número: "))
print(numero * 1)
print(numero * 2)
print(numero * 3)
print(numero * 4)
print(numero * 5)
print(numero * 6)
print(numero * 7)
print(numero * 8)
print(numero * 9)
print(numero * 10)

## Ejercicio 7

## Ingrese un valor entero distinto a cero.
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
## Operaciones 
print(f"La suma de {numero1} y {numero2} es {numero1 + numero2}.")
print(f"La resta de {numero1} y {numero2} es {numero1 - numero2}.")
print(f"La multiplicación de {numero1} y {numero2} es {numero1 * numero2}.")
print(f"La división de {numero1} y {numero2} es {numero1 / numero2}.")

## Ejercicio 8

altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
indiceDeMasaCorporal = peso // (altura ** 2)
print(f"Su índice de masa corporal es {indiceDeMasaCorporal}")

## Ejercicio 9

temperaturaEnCelsius = float(input("Ingrese la temperatura en Celsius: "))
temperaturaEnFahrenheit = (temperaturaEnCelsius * 9/5) + 32
print(f"La temperatura en Fahrenheit es: {temperaturaEnFahrenheit}")

## Ejercicio 10

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio es: {promedio}")
