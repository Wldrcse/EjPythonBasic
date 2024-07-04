# Documentación: https://docs.python.org/es/3/library/math.html
import math as m # Agregando un alias
print('** Área del Círculo  **')
radio = float(input("Ingrese el radio del círculo: "))
# Importamos 2 funciones: pi y pow
AreaCir = m.pi*m.pow(radio,2)
print(f"El área del círculo es {AreaCir:.2f}")

print("Calcular la hipotenusa de un triángulo rectángulo")
co = float(input("Ingrese el cateto opuesto: "))
ca = float(input("Ingrese el cateto adyacente: "))
hipo = m.sqrt( m.pow(co,2) + m.pow(ca,2) )
print(f"La hipotenusa es {hipo}")