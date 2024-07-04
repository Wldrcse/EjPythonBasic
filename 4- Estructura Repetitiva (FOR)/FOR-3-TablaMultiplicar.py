# Tabla de Multiplicar del número ingresado 4 x 5 = 20
n = int(input("Ingrese un número para mostra la tabla de multiplicar: "))
print(f"Tabla del {n}")
for i in range (1,13):
    print(f"{n} x {i} = {n*i}")