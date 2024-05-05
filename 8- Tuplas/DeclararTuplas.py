# Colecciones Inmutables

# Crear tupla empleando paréntesis
lenguajes = ('Python', 'Php', 'Java', 'R', 'C++') 

# Crear tupla emplenado Constructor tuple
estaciones = tuple(('Primavera', 'Verano', 'Invierno', 'Otoño'))

# Crear tupla Sin agregar ningún símbolo
colores = 'Rojo', 'Verde', 'Amarillo', 'Azul'

# Crear tupla desde una lista
valores_lista =[1, 2, 3, 4] # Declaramos una Lista
valores_tupla = tuple(valores_lista) # Convertimos en tupla
print(f"Tupla: {valores_tupla}") # Imprimimos el contenido de la tupla

# Crear tupla desde una cadena de caracteres
texto = "SENATI"
tupla_texto = tuple(texto)
print(f"Tupla desde una cadena de caracteres: {tupla_texto}")

# Formas de Imprimir
print(f"Tupla: {lenguajes}")
print(f"Mostrar con índice: {lenguajes[0]}")
print(f"Desde el índice 1 hasta el 3: {lenguajes[1:4]}")
print(f"Mostrar con índice negativo: {lenguajes[-1]}")
for i in lenguajes:
    print(f"Lenguaje de Programación: {i}")
    
