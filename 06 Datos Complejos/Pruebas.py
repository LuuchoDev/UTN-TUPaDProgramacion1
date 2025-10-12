contactos = {}
for i in range(1):
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
    print(f"El contacto {nombre_buscar} tiene el numero {telefono}")