#Leer dos números y decir cual es mayor y cual es menor.

num1 = int(input("numero 1? "))
num2 = int(input("numero 2? "))

if num1 == num2:
    print("Ambos numero son iguales")
elif num1 > num2:
    print(f'El numero mayor es {num1} y el menor {num2}')
else:
    print(f'El numero mayor es {num2} y el menor {num1}')