notas = {'n1': 15, 'N2': 19, 'n3': 10, 'n4': 12}
suma = 0
for i in notas.values():
    suma = suma + i
prom = suma / len(notas)
print(f"Promedio: {prom}")
if ( prom >= 10.5 ):
    print("Aprobado")
else:
    print("Desaprobado")
m = input("Ingrese la nota a modificar: ")
temp = int(input("Ingrese la nueva nota: "))
notas[m.upper()] = temp
suma = 0
for i in notas.values():
    suma = suma + i
prom = suma / len(notas)
print(suma)
print(notas)
print(f"Promedio: {prom}")
total = sum(notas.values())
print(f"Total: {total}")