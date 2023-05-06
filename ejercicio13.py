renta_anual = float(input("Ingrese su renta anual: "))

if renta_anual < 10000:
    impuesto = 0.05
elif renta_anual >= 10000 and renta_anual < 20000:
    impuesto = 0.15
elif renta_anual >= 20000 and renta_anual < 35000:
    impuesto = 0.20
elif renta_anual >= 35000 and renta_anual < 60000:
    impuesto = 0.35
else:
    impuesto = 0.45

print(f"Le corresponde pagar de impuesto: {impuesto*100}%")

