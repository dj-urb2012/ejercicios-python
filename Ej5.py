#Mostrar los numero pares comprendidos entre un valor inicial y un valor final de números
#enteros.

inicio = 5
fin = 100

for i in range(inicio, fin + 1):
    if i % 2 == 0:
        print(i)
    else:
        continue