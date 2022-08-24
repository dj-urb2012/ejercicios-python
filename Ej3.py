#Aplicar el IVA al precio de un producto.

precioPro = int(input("Ingrese el precio del producto: "))
iva = precioPro * 0.15

print("El iva del producto es:", iva)
print("El total a pagar es:", precioPro + iva)