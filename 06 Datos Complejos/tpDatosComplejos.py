# ==========================================
#               EJERCICIO 1
# ==========================================
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
## Agrega nuevas frutas y sus precios
precios_frutas['Naranja'] = 1200
precios_frutas["manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)

# ==========================================
#               EJERCICIO 2
# ==========================================
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
## Agrega nuevas frutas y sus precios
precios_frutas['Naranja'] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)
## Actualiza los precios de las frutas 
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
print(precios_frutas)

# ==========================================
#               EJERCICIO 3
# ==========================================

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
## Agrega nuevas frutas y sus precios
precios_frutas['Naranja'] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)
## Actualiza los precios de las frutas 
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
print(precios_frutas)

lista_frutas = precios_frutas.keys()
print(lista_frutas)

# ==========================================
#               EJERCICIO 4
# ==========================================
contactos = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input(f"Ingrese el teléfono del contacto {nombre}: ")
    contactos[nombre] = telefono
    print(f"Contacto agregado: {nombre} - {telefono}")

print("\nLista de contactos: ")
lista_contactos = contactos.keys()
print(lista_contactos)
print("\nBúsqueda de contactos:")
nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
if nombre_buscar in contactos:
    print(f"El contacto {nombre_buscar} tiene el numero {contactos[nombre_buscar]}")
else:
    print(f"El contacto {nombre_buscar} no está en la lista.")

# ==========================================
#               EJERCICIO 5
# ==========================================
frase = input("Ingrese una frase: ")
palabras = frase.lower().split()

## Crear un conjunto para almacenar palabras únicas
palabras_unicas = set(palabras)
print("Palabras únicas en la frase:")
print(palabras_unicas)

## Cuenta las palabras y la guarda en un diccionario
contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
print("Contador de palabras:")
print(contador)

# ==========================================
#               EJERCICIO 6
# ==========================================
alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}:")
    nota_temporal = []
    for j in range (3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        nota_temporal.append(nota)
    alumnos[nombre] = tuple(nota_temporal)
    print(f"Notas de {nombre} guardada.")

print("\nPromedios de los alumnos:")
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {alumno} es: {promedio}")
    
# ==========================================
#               EJERCICIO 7
# ==========================================

