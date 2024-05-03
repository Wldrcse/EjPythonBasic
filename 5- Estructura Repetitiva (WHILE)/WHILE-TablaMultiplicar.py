# Tabla de Multiplicar del número ingresado 4 x 5 = 20 Empleando While
n = int(input("Ingrese un número para mostra la tabla de multiplicar: "))
i = 1
print(f"Tabla del {n}")
while ( i <= 12):
    print(f"{n} x {i} = {i*n}")
    i += 1