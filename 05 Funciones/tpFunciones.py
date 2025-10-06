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