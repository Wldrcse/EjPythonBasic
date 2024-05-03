def Ordenar(a,b,c):
    print("Números ordenados de mayor a menor")
    mayor = max(a,b,c)
    menor = min(a,b,c)
    medio = a + b + c - mayor - menor
    print(f'Números ordenados de mayor a menor: {mayor}, {medio}, {menor}')
n1 = int(input("Ingrese número 1: "))
n2 = int(input("Ingrese número 2: "))
n3 = int(input("Ingrese número 3: "))
Ordenar(n1,n2,n3)
