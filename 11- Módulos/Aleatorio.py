from random import *
rp = True
cant = 1
while (rp):
    numeroAleatorio =randint(1,100)
    print("Adivinar el número aleatorio generado entre: 1 al 100")
    while (True):
        n = int(input("Ingrese un número: "))
        if (numeroAleatorio == n ):
            print(f"Lograste encontrar el número en {cant} intentos")
            break
        else:
            cant += 1
            if (numeroAleatorio > n):
                print("Debe ser un número mayor!")
            else:
                print("Debe ser un número menor!")
    resp = input("Desea continuar S/N: ")
    resp = resp.upper()
    if ( resp != 'S'):
        rp = False     