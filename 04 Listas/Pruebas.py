
## Ejercicio 10:


ventas = [
    [100, 250, 3100, 4200],
    [60, 35, 120, 600],
    [5, 15, 45, 10],
    [1100, 300, 400, 500],
    [8, 5, 2, 60],
    [20, 10, 5, 8],
    [200, 180, 350, 700]
] 
productos_nombre = ['Cuaderno', 'Termo', 'Mate', 'Lapiz']

ventas_producto_por_dia = [[], [], [], []]

for dia in ventas:
    for i, producto in enumerate(dia):
        ventas_producto_por_dia[i].append(producto)

print('Total vendido por cada producto:')
for i, ventas_producto in enumerate(ventas_producto_por_dia):
    print(f'\t{productos_nombre[i]}: {sum(ventas_producto)}')


mayor_ventas_dia = [None, None] 
for i, dia in enumerate(ventas):
    total_ventas = sum(dia)
    if mayor_ventas_dia[1] == None or mayor_ventas_dia[1] < total_ventas:
        mayor_ventas_dia = [i, total_ventas]

print(f'\nDía con mayores ventas totales: {mayor_ventas_dia[0] + 1} (con {mayor_ventas_dia[1]})')


mayor_ventas_producto = [None, None] 
for i, producto in enumerate(ventas_producto_por_dia):
    total_ventas = sum(producto)
    if mayor_ventas_producto[1] == None or mayor_ventas_producto[1] < total_ventas:
        mayor_ventas_producto = [i, total_ventas]

print(f'\nProducto más vendido en la semana: {productos_nombre[mayor_ventas_producto[0]]} (con {mayor_ventas_producto[1]})')