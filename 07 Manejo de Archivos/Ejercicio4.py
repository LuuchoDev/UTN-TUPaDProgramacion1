productos = []
with open("07 Manejo de Archivos\productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
print(productos)