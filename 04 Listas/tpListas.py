## Ejercicio 1
notas = [10, 8, 7, 6, 10, 4, 8, 7, 6, 5]
print(f"Notas de los estudiantes: {notas}")

## Calcular y mostrar el promedio de las notas
promedio = sum(notas) / len(notas)
print(f"Promedio de las notas: {promedio}")

## Indicar la nota más alta y la más baja
print(f"La nota mas alta es: {max(notas)}")
print(f"La nota mas baja es: {min(notas)}")

## Ejercicio 2

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
        
## Ejercicio 3