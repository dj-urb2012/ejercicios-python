#Leer x cantidad de precios y mostrar el precio mas alto y el precio más bajo.

precios = []

res = "SI"
while res.upper() == "SI":
    precio = int(input("Precio: "))
    precios.append(precio)
    res = input("Desea agregar otro precio: SI - NO ")
precios.sort()
print("El precio mas bajo es:", precios[0])
print("El precio mas alto es:", precios[len(precios) - 1]) 