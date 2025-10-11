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
