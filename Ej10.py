"""Dado el numero de cuenta, el saldo y el monto de retiro de una cuenta de ahorra verifique
si la persona puede realizar el retiro. Una vez evaluado debe mostrarse el saldo que queda
después del retiro."""

def verificar(saldo, monto):
    if saldo == 0 or (saldo - monto) <= 0:
        return False
    else: return True

numeroCuenta = "00002032113"
saldo = 1000

monto = int(input("Ingrese el monto de retiro: "))
puedeRetirar = verificar(saldo, monto)
if puedeRetirar == True:
    print("El saldo restante es:", saldo - monto)
else: print("No se puede retirar dinero, saldo insuficiente")