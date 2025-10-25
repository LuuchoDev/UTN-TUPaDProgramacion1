with open("07 Manejo de Archivos\productos.txt", "a") as archivo:
    producto = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: ")
    cantidad = input("Ingrese la cantidad del producto: ")
    archivo.write(f"{producto},{precio},{cantidad}\n")