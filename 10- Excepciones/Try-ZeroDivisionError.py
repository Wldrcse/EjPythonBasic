rp = True
while ( rp ):
    while ( True ):
        print('''
 _________________________
| ** MENÚ DE OPCIONES **  |
| 1- Suma                 |
| 2- Resta                |
| 3- Multiplicación       |
| 4- División             |
| 5- Salir                |
|_________________________|''')
        try:
            op = int(input("Ingrese una opción: "))
            break
        except:
            print("No ha ingresado un número, vuelva a intentarlo!")
    op = int(op)
    if ( op >= 1 and op <= 4 ):
        while ( True ):
            try:
                a = float(input("Ingrese un número: "))
                b = float(input("Ingrese otro número: "))
                break
            except:
                print("No ha ingresado números, inténtelo de nuevo!")
        print(f"Números ingresados: {a}, {b}")
        if ( op == 1 ):
            print(f"La suma de los números ingresados es: { a + b }")
        elif ( op == 2 ):
            print(f"La resta de los números ingresados es: { a - b }")
        elif ( op == 3 ):
            print(f"El producto de los números ingresados es: { a * b }")
        else:
            try:
                print(f"La división de los números ingresados es: { a / b }")
            except ZeroDivisionError:
                print("No es posible dividir entre cero!")
    elif ( op == 5 ):
        print("Saliendo del programa!")
        rp = False
    else:
            print("No es una opción del menú, vuelva a intentarlo!")
