"""Leer los datos de un estudiante como el nombre, los apellidos, la carrera y su promedio.
Evaluar si apto para beca, el estudiante podrá optar a beca si su promedio es mayor a 85
en todas las carreras excepto Ingeniería de Sistemas donde su promedio debe ser mayor a
95."""

nombres = input("Escribe tus nombre: ")
apellidos = input("Escribe tus apellidos: ")
promedio = int(input("Ingresa tu promedio: "))
carrera = input("Escribe el nombre de la carrera completo y en minusculas: ")

if carrera == "ingenieria en sistemas de informacion":
    if promedio > 95:
        print("Eres apto para beca")
    else:
        print("No eres apto para beca")
else:
    if promedio > 85:
        print("Eres aptop para beca")
    else:
        print("No eres aptop para beca")