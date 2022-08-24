#Calcular la edad de una persona.

anioNac = int(input("Ingrese su anio de nacimiento: "))
edad = 2022 - anioNac

if edad <= 0 or edad > 100:
    print("Anio de nacimiento invalida")
else:
    print(f'Usted tiene o cumplira {edad} anios de edad')    

