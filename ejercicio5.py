cantidad = float(input("Indique cantidad de dinero a invertir: "))
interes = float(input("Indique le interés anual: "))
anios = int(input("Indique total de años para obtener el retorno: "))
capital = cantidad * (1 + (interes/100))**anios

print(f"El capital obtenido después de {anios} años es: {capital}")