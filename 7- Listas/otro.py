def Evaluar( prom ):
    if ( prom >= 10.5 ):
        print("Aprobado!")
    else:
        print("Desaprobado!")
notas = [] # Lista vacía
n = int(input("Cuántas notas desea registrar?: "))
for i in range (n):
    rp = True
    while (rp):
        temp = float(input(f"Ingrese nota {i+1}: "))
        if ( temp >= 0 and temp <= 20 ):
            notas.append(temp)
            rp = False
        else:
            print("Error, solo notas entre 0 al 20")
suma = sum(notas)
prom = suma / n
print(f"Notas ingresadas: {notas}")
print(f"Promedio Final: {prom:.2f}")
Evaluar(prom)
