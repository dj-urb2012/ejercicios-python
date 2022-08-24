"""Dado el primer nombre, segundo nombre, primer apellido y el segundo apellido de un
estudiante de manera individual, escriba un código en Python que permita crear un correo
electrónico utilizando la siguiente sintaxis: primer nombre + punto (.) + primer apellido +
“@est.uca.edu.ni”"""

primerNom = input("Ingrese su primer nombre: ")
segundoNom = input("Ingrese su segundo nombre: ")
primerApellido = input("Ingrese su primer apellido: ")
segundoApellido = input("Ingrese su segundo apellido: ")

print(f'Se le ha asignado la siguiente direccion de correo: {primerNom.lower()}.{primerApellido.lower()}@est.uca.edu.ni')