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
