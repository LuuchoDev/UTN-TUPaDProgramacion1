## Ejercicio 1

for i in range(101):
    print(i)
    
## Ejercicio 2

num = int(input("Ingrese un número: "))

## Convierto el numero a string y cuento la cantidad de digitos
cantDigitos = len(str(num))

## Imprimo la cantidad de dígitos                         
print("La cantidad de dígitos es:", cantDigitos)    

## Ejercicio 3

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

## Determino el menor y el mayor
menor = min(num1, num2)
mayor = max(num1, num2)

## Calculo la suma de los números entre el menor y el mayor
suma = 0
for i in range (menor + 1 , mayor):
    suma += i
print(f"La suma de los números entre {menor} y {mayor} es: {suma}")

## Ejercicio 4

