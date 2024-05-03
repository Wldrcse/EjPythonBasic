def Sumar(n,m):
    return (n+m)
def Restar(n,m):
    return (n-m)
def Multiplicar(n,m):
    print(f"El producto de los números ingresados es: {n*m}")
def Dividir(n,m):
    if(m!=0):
        print(f"La división de los números ingresados es: {n/m:.2f}")
    else:
        print("No se puede dividir entre cero!")
menu = '''**  Menú de Opciones  **
1- Suma
2- Resta
3- Multiplicación
4- División
5- Salir'''
print(menu)
op = int(input("Ingrese una opción: "))
if ( op >= 1 and op <= 4 ):
    n1 = float(input("Ingrese un número: "))
    n2 = float(input("Ingrese otro número: "))
    if ( op == 1 ):
        result = Sumar(n1, n2)
        print(f"La suma de los números ingresados es: {result}")
    elif ( op == 2 ):
        result = Restar(n1, n2)
        print(f"La resta de los números ingresados es: {result}")
    elif ( op == 3 ):
        Multiplicar(n1, n2)
    else:
        Dividir(n1, n2)
else:
    print("No es una opción correcta, el programa ha concluido!")