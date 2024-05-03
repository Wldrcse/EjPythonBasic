x = int(input("Ingrese un número del 1 al 5: "))

# Esto es similar al Switch
match x:
    case 1: print("Número ingresado: Uno"),
    case 2: print("Número ingresado: Dos"),
    case 3: print("Número ingresado: Tres"),
    case 4: print("Número ingresado: Cuatro"),
    case 5: print("Número ingresado: Cinco"),
    case _: print("Error de ingreso")
    