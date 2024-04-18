# Calcular el IMC de una persona
peso = float(input("Ingrese su peso en Kg: "))
talla = float(input("Ingrese su talla en m: "))
imc = peso/(talla**2)
print("Su Índice de Masa Corporal es: {0:.2f}".format(imc)) # Mostrar solo 2 decimales
