# Ingresar un número del 5 al 10
cond = True
while(cond):
    n = int(input("Ingrese un número del 5 al 10: "))
    if ( n >= 5 and n <= 10 ):
        print(f"El Número {n} se encuentra en el rango indicado, gracias.")
        cond = False
    else:
        print("El número ingresado no se encuentra en el rango indicado, vuelva a intentarlo!")