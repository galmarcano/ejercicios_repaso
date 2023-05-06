edad_minima = 16
ingresos_tope = 1000

anios = int(input("Ingrese su edad: "))
ingreso = float(input("¿Cuál es su ingreso mensual? "))

if anios > edad_minima and ingreso >= ingresos_tope:
    print("Tiene que tributar")
else:
    print("No tiene que tributar")