lista = []
n = int(input("Cuantos números desea sumar?: "))
suma = 0
for i in range (1, n+1):
    temp = int(input(f"Ingrese número {i}: "))
    lista.append([temp])
    suma = suma + temp
print(f"Los números ingresados son: {lista}")
print(f"La suma de los números ingresados es: {suma}")
print(f"El promedio de los números ingresados es: {suma/n:.2f}")
