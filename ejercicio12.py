nombre = str(input("Ingrese su nombre: "))
sexo = str(input("Ingrese su sexo (F o M): "))

if sexo == "M":
    if nombre[0].lower() < "m":
        print("Perteneces al grupo A")
    else:
        print("Perteneces al grupo B")
else:
    if nombre[0].lower() > "n":
        print("Perteneces al grupo A")
    else:
        print("Perteneces al grupo B")
