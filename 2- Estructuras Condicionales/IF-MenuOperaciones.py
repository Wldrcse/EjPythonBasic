# texto = ("Menú de Opciones\n"
#          "1- Suma\n"
#          "2- Resta\n"
#          "3- Multiplicación\n"
#          "4- División")
# print(texto)        
# ************** Agregar comentario Ctrl + K + C
# ************** Quitar comentario Ctrl + K + U
##
print('''
Menú de Opciones
1- Suma
2- Resta
3- Multiplicación
4- División''')
op = int(input("Ingrese una opción: "))
if ( op >= 1 and op <= 4): # operador and Para agregar 2 condiciones
    num1 = float(input("Ingrese un número: "))
    num2 = float(input("Ingrese otro número: "))
    if ( op == 1):
        print(f"La suma de los números ingresados es: {(num1+num2):.2f}")
    elif ( op == 2):
        print(f"La resta de los números ingresados es: {(num1-num2):.2f}")
    elif ( op == 3):
        print(f"La multiplicación de los números ingresados es: {(num1*num2):.2f}")
    else:
        if ( num2 != 0):
            print(f"La división de los números ingresados es: {(num1/num2):.2f}")
        else:
            print("No se puede dividir entre 0")
else:
    print("Error al indicar opción, el programa ha concluido!")
