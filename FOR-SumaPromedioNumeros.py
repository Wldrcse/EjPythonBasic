# Sumar números ingresados por pantalla
n = int(input("Cuantos números desea sumar: "))
suma = 0
for i in range(n):
    num = float(input("Ingrese número: "))
    suma = suma + num
# Versión 1 para mostrar
print("La suma de los números ingresados es {0:.2f}".format(suma))
print("El promedio de los números ingresados es {0:.2f}".format(suma/n))
# Versión 1 para mostrar
print(f"La suma de los números ingresados es {suma:.2f}")
print(f"El promedio de los números ingresados es {suma/n:.2f}")