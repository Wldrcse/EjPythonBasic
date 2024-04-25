# Calcular el IMC de una persona
peso = float(input("Ingrese su peso en Kg: "))
talla = float(input("Ingrese su talla en m: "))
imc = peso/(talla**2)
print(f"Su Índice de Masa Corporal es: {imc:.2f}") # Mostrar solo 2 decimales
if ( imc < 18.5 ):
    print("Condición: Bajo Peso")
elif ( imc <= 24.9 ):
    print("Condición: Normal")
elif ( imc <= 29.9 ):
    print("Condición: Sobrepeso")
elif ( imc <= 34.9 ):
    print("Condición: Obesidad I")
elif ( imc <= 39.9 ):
    print("Condición: Obesidad II")
else:
    print("Condición: Obesidad III")

