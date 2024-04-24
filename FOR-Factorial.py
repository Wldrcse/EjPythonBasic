# Calcular el factorial número ingresado por el usuario
n = int(input("Ingresar un número para calcular el factorial: "))
fact = 1
for i in range(1,n+1):
    fact = fact*i
    
# Para mostrar los resultados
# Forma 1
print("El factorial de {0} es {1}".format(n,fact)) 
# Forma 2
print("El factorial de {} es {}".format(n,fact)) 

# Si deseamos mostrar con decimales el factorial
# Forma 1
print("El factorial de {0} es {1:.2f}".format(n,fact))
# Forma 2
print("El factorial de {} es {:.2f}".format(n,fact))
