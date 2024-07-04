# Declarar Función Comparar
def Comparar ( a, b ):
    if (a > b ):
        print(f"El mayor es {a}")
        print(f"El menor es {b}")
    elif (b > a ):
        print(f"El mayor es {b}")
        print(f"El menor es {a}")
    else:
        print("Los números son iguales!")

n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese otro número: "))
Comparar( n1, n2 ) # Invocar a la función