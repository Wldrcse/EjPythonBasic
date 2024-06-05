# Controlar que las notas ingresadas se encuentren entre 0 y 20
notas = [] # Lista vacía
suma = 0
n = int(input("Cuántas notas desea registrar?: "))
for i in range (n):
    temp = float(input(f"Ingrese nota {i+1}: "))
    notas.append(temp)
    suma = suma + temp
prom = suma / n
print(f"Notas ingresadas: {notas}")
print(f"Promedio: {prom:.2f}")
if ( prom >= 10.5 ):
    print("Aprobado!")
else:
    print("Desaprobado!")
# Controlar que las notas ingresadas se encuentren entre 0 y 20
"""
notas = [] # Lista vacía
suma = 0
n = int(input("Cuántas notas desea registrar?: "))
for i in range (n):
    rp = True
    while (rp):
        temp = float(input(f"Ingrese nota {i+1}: "))
        if ( temp >= 0 and temp <= 20 ):
            notas.append(temp)
            suma = suma + temp
            rp = False
        else:
            print("Error, solo notas entre 0 al 20")
    
prom = suma / n
print(f"Notas ingresadas: {notas}")
print(f"Promedio: {prom:.2f}")
if ( prom >= 10.5 ):
    print("Aprobado!")
else:
    print("Desaprobado!")
eliminar = float(input("Ingrese la nota a eliminar: "))
for i in range(n):
    if ( eliminar == notas[i] ):
        print(f"Nota encontrada, se procederá a eliminar!")
        notas.remove(eliminar)
        suma = suma - eliminar
        print(f"Notas ingresadas: {notas}")
        prom = suma/len(notas)
        print(f"Promedio final: {prom:.2f}")
        if ( prom >= 10.5 ):
            print("Aprobado!")
        else:
            print("Desaprobado!")
        break
else:
    print("Error, nota no encontrada!")


    """