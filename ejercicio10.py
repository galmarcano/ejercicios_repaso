numerador = float(input("Ingrese el numerador: "))
denominador = float(input("Ingrese el denominador: "))

if denominador == 0:
    print("No se puede dividir entre cero")
else:
    resultado = numerador/denominador
    print(resultado)