# Solicitar al usuario un número, si el número ingresado es par, mostrar desde el 2 hasta el número ingresado
# en el caso de ingresar un número impar, mostrar desde el 1 hasta el número ingresado
#### Versión 1
n = int(input("Ingresar un número: "))
if ( n % 2 == 0 ):
    for i in range(2, n+1, 2):
        print(i)
else:
    for i in range(1, n+1, 2):
        print(i)
    
#### Versión 2
n = int(input("Ingresar un número: "))
if ( n % 2 == 0 ):
    j = 2
else:
    j = 1
for i in range(j, n+1, 2):
    print(i)