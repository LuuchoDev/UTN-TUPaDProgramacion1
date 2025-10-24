agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}

dia = input('Ingrese el dia: ')
hora = input('Ingrese la hora: ')
evento = agenda.get((dia, hora), 'No hay evento en ese dia y hora')
print(evento)
