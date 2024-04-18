n = int(input("Ingrese un número: "))
if ( n < 0 ): # Si el número es menor a 0 multiplicamos por -1
    n = n * (-1)
if ( n < 10 ):
    print("El número tiene 1 dígito")
elif ( n < 100 ):
    print("El número tiene 2 dígitos")
elif ( n < 1000 ):
    print("El número tiene 3 dígitos")
elif ( n < 10000 ):
    print("El número tiene 4 dígitos")
else:
    print("El número tiene más de 4 dígitos")