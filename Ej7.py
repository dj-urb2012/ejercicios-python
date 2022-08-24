#Leer x cantidad de edades y mostrar el promedio de dichas edades.

edades = []

res = "SI"

while res.upper() == "SI":
    edad = int(input("Edad? "))
    edades.append(edad)
    res = input("Desea agregar otra edad - SI - NO ")

print(f'El promedio de edad es de {sum(edades) / len(edades)}')