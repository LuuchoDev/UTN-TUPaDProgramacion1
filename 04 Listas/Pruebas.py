## Lista de alumnos
alumnos = ["Ana", "Luis", "Carlos", "Marta", "Lucía", "Jorge", "Sofía", "Diego"]
print(alumnos)

## Consulta al usuario si desea agregar un nuevo alumno o eliminar uno existente.
Agregar_O_Eliminar = input("¿Desea agregar un nuevo alumno (a) o eliminar uno existente (e)? (a/e): ")
if Agregar_O_Eliminar in 'aA':
    ## Solicita el nombre del nuevo alumno
    nuevo_alumno = input("Ingrese el nombre del nuevo alumno: ")
    alumnos.append(nuevo_alumno)
    print(f"Alumno '{nuevo_alumno}' agregado.")
elif Agregar_O_Eliminar in 'eE':
    ## Solicita el nombre del alumno a eliminar
    alumno_a_eliminar = input("Ingrese el nombre del alumno que desea eliminar: ")
    ## Verifica si el alumno está en la lista antes de eliminarlo
    if alumno_a_eliminar in alumnos:
        alumnos.remove(alumno_a_eliminar)
        print(f"Alumno '{alumno_a_eliminar}' eliminado.")
    else:
        print(f"Alumno '{alumno_a_eliminar}' no encontrado en la lista.")

print(f"La lista actualizada es: {alumnos}")