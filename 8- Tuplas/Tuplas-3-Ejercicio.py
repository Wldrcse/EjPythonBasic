# Mostrar el promedio de notas almacenadas en una tupla, luego indicar si el alumno ha aprobado o desaprobado
notas = 20,5,10,8,16
suma = 0
for i in notas:
    suma = suma + i
prom = suma / len(notas)
print(f"Promedio Final: {prom}")
if ( prom >= 10.5 ):
    print("Estado: Aprobado")
else:
    print("Estado: Desaprobado")

# Obtener la menor y mayor nota del alumno
mayor = notas[0]
menor = notas[0]
# Modificar el for
for i in notas:
    suma = suma + i
    if ( mayor < i ):
        mayor = i
    if (menor > i ):
        menor = i
print(f"Nota mayor: {mayor}")
print(f"Nota menor: {menor}")
may = max(notas)
men = min(notas)
print(f"Nota mayor: {may}")
print(f"Nota menor: {men}")
