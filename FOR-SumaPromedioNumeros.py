# Sumar números ingresados por pantalla
n = int(input("Cuantos números desea sumar: "))
suma = 0
for i in range(n):
    num = float(input("Ingrese número: "))
    suma = suma + num
print("La suma de los números ingresados es {0:.2f}".format(suma))
print("El promedio de los números ingresados es {0:.2f}".format(suma/n))