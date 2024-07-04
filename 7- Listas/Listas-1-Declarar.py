# Declarar una Lista utilizar Corchetes
datos = ["Texto", 4, 12.5, True, ['a', 'b', 'c'], {"Rojo":"Red", "Verde": "Green"}]
#        |_____| |_| |___| |___|  |___________|    |____________________________|
# Índice    0     1    2     3           4                     5

# Declarar un lista
lp = ["Java", "PHP", "Python", "C++", "R"]

# Mostrar todos los elementos de la lista
print(f"Todos los elementos de la lista lp: {lp}")

# Declarar lista empleando el constructor list()
dias = list(["Lunes", "Martes", "Miércoles"])
print(dias)

# Crear lista desde un constructor de la clase list(iterable)
lista =("SENATI") # lista = "SENATI"
lista_texto = list(lista)
print(lista_texto)

# Crear lista desde una tupla
colores_tupla = ('Rojo', 'Verde', 'Amarillo', 'Azul') # Tupla
print(type(colores_tupla))
print(f"Tupla de colores: {colores_tupla}")
colores_lista = list(colores_tupla)
print(type(colores_lista))
print(f"Lista colores: {colores_lista}")

print(f"Todos los elementos de la lista lp: {datos}") # Imprimir toda la lista
print(f"Mostrar solo el primer elemento de la lista: {datos[0]}") # Para imprimir un elemento
print(f"Mostrar un elemento de una sublista: {datos[4][0]}") # Imprimir los elementos de una sub lista
print(f"Mostrar un elemento de una sublista: {datos[4][2]}") # Imprimir los elementos de una sub lista
print(f"Imprimir desde un índice señalado:  {datos[1:3]}") # Imprimir desde el índice 1 hasta un valor inferior al declarado
print(f"Imprimir desde un índice señalado con incrementos datos: {datos[1:6:2]}") # Imprimir desde el índice 1 hasta un valor inferior al declarado, incremento de 2 en 2
print(f"Imprimir un valor de un diccionario: {datos[5]["Rojo"]}") # Para imprimir un valor de un diccionario
print(f"Imprimir un elemento considerando el orden inverso: {datos[-1]}") # Permite imprimir desde el final

# Modificar elementos de la lista
print(f"Lista original: {datos}")

# Modificar el elemento del índice 0
datos[0] = "SENATI"
print(f"Lista modificada: {datos}")

# Modificar varios elementos desde un índice señalado, hasta otro que corresponda, si el índice es mayor, elimina otros elementos.
datos[1:4] = [111, 222, 333]
print(f"Lista modificada: {datos}")

# Si el índice es mayor, elimina también los elementos
datos[1:6] = [111, 222, 333]
print(f"Lista modificada: {datos}")

# Modificar varios elementos desde un índice señalado y eliminar el resto de elementos
datos[1:] = [66, 99, 55]
print(f"Lista modificada: {datos}")

# Mostrar elementos empleando for
for i in datos:
    print(f"Elementos: {i}")

# Es posible unir dos listas
lista1 = [1,2,3]
lista2 = [4,5,6,7]
lista3 = lista1+ lista2
print(f"Concatenando listas: {lista3}")