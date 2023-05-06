pizza_veg = ["pimiento", "tofu"]
pizza_no_veg = ["pepperoni", "jamon", "salmon"]
base_pizza = ["tomate", "mozarella"]

tipo_pizza = str(input("¿Qué tipo de pizza quiere (vegetariana/ no vegetariana? "))

if tipo_pizza == "vegetariana":
    print(pizza_veg)
else:
    print(pizza_no_veg)

ingrediente = (str(input("¿Qué ingrediente quieres? ")))
print(f"Su pizza es {base_pizza} con {ingrediente}")

