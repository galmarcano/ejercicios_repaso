puntuacion = float(input("Ingrese la puntuación del empleado: "))

if puntuacion == 0.0:
    nivel_rendimiento = "Inaceptable"
    dinero_a_recibir = 2400*puntuacion
    print("Su nivel de rendimiento es:", nivel_rendimiento, "y recibirás un bono de:", dinero_a_recibir)

elif puntuacion == 0.4:
    nivel_rendimiento = "Aceptable"
    dinero_a_recibir = 2400*puntuacion
    print("Su nivel de rendimiento es:", nivel_rendimiento, "y recibirás un bono de:", dinero_a_recibir)

elif puntuacion >= 0.6:
    nivel_rendimiento = "Meritorio"
    dinero_a_recibir = 2400*puntuacion
    print("Su nivel de rendimiento es:", nivel_rendimiento, "y recibirás un bono de:", dinero_a_recibir)

else:
    print("Solo se aceptan niveles de rendimiento: 0.0, 0.4, 0.6 o mayores a 0.6")

