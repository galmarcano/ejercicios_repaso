interes = 0.04

monto_inicial = float(input("Ingrese el monto inicial a invertir: "))

saldo_año1 = monto_inicial*interes + monto_inicial
saldo_año2 = saldo_año1*interes + saldo_año1
saldo_año3 = saldo_año2*interes + saldo_año2

print(f"El retorno de la inversión tras el primer año es {round(saldo_año1, 2)}$")
print(f"El retorno de la inversión tras el segundo año es {round(saldo_año2, 2)}$")
print(f"El retorno de la inversión tras el tercer año es {round(saldo_año3, 2)}$")