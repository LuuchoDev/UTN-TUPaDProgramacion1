def leer_productos():
    productos = []
    with open("07 Manejo de Archivos\productos.txt", "r") as archivo:
        for linea in archivo:
            producto, precio, cantidad = linea.strip().split(",")
            productos.append({"nombre": producto, "precio": precio, "cantidad": cantidad})
    return productos

def buscar_producto(producto, nombre_productos):
    for producto in producto:
        if producto["nombre"].lower() == nombre_productos.lower():
            return producto
    return None

def guardar_productos(productos):
    with open('07 Manejo de Archivos\productos.txt', 'w') as file:
        for producto in productos:
            file.write(f'{producto["nombre"]},{producto["precio"]},{producto["cantidad"]}\n')

def agregar_producto(productos):
    nombre = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: ")
    cantidad = input("Ingrese la cantidad del producto: ")
    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    return productos

productos = leer_productos()
print(productos)

producto = buscar_producto(productos, "Manzana")
print(producto)

producto = agregar_producto(productos)
guardar_productos(productos)
