peso_payaso = 112
peso_muñeca = 75

num_payasosx = int(input("Ingrese cantidad de payasos para el paquete: "))
num_muñecasx = int(input("Ingrese cantidad de muñecas para el paquete: "))

peso_total = peso_payaso*num_payasosx + peso_muñeca*num_muñecasx

print(f"Peso total del pedido es {peso_total}g")