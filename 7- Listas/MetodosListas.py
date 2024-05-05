# Declarar un lista
lp = ["Java", "PHP", "Python", "C++", "R"]

# Append() Este método nos permite agregar nuevos elementos a una lista, de uno en uno, las ubica al final de la lista.
print("Método Append")
print(f"Lista original: {lp}")
lp.append("JavaScript")
print(f"Lista modificada: {lp}")
lp.append([15,4,8]) # Esto agrega como un solo elemento
print(f"Lista modificada: {lp}")

# Extend() Permite agregar varios elementos dentro de una lista, las ubica al final de la lista
print("Método Extend")
lp.extend([8,5,12])
print(f"Lista modificada: {lp}")

#Insert() Permite agregar un elemento en una posición determinada, emplea el índice para esto
print("Método Insert")
lp.insert(0,"Kotlin")
print(f"Lista modificada: {lp}")

# Remove() Permite eliminar un elemento que se le pase como parámetro de la lista a donde se le esté aplicando.
print("Método Remove")
lp.remove("R")
print(f"Lista Elimina R: {lp}")

# Del() Elimina un elemento teniendo en cuenta el índice
print("Método Del")
del(lp[1])
print(f"Lista eliminando el índice 1: {lp}")
# Si no se incluye el índice este método elimina la lista

# Pop() Extrae y elimina un elemento de la lista en la posición indicada.
print("Método Pop")
print(lp.pop(0))
print(lp)

# Index() Devuelve el número de índice del elemento que le pasemos por parámetro.
print("Método Index")
print(f"Índice de Python: {lp.index("Python")}")

# Agregamos más elementos
lp.extend(["Python", "Python", "Python"])

# Count() Permite saber cuántas veces un elemento de una lista se repite
print("Método Count")
print(lp)

# Contamos cuantas veces se repite Python
print(f"Python se repite {lp.count("Python")} veces")

# Para copiar una lista 
lp_copia = lp.copy()
print(f"Copia de la lista lp: {lp_copia}")

# Reverse() Permite invertir los elementos de una lista.
print("Método Reverse")
lp_inv = lp_copia
lp_inv.reverse()
print(f"Lista invertida: {lp_inv}")

# Len() Permite indicar la cantidad de elementos de una lista
print("Método Len")
print(f"La lista tiene {len(lp)} elementos")

# Clear() Permite eliminar todos los elementos de una lista
lp_copia.clear()
print(f"Lista vacía: {lp_copia}")

# Sort() Permite ordenar elementos de una lista, todos los elementos deben ser del mismo tipo de dato, textos o números
lista = ['S','E','N','A','T','I']
print(f"Lista orginal: {lista}")
lista.sort()
print(f"Lista ordenada Ascendente: {lista}")

# Si se desea ordenar de manera descendente
lista.sort(reverse=True)
print(f"Lista ordenada Descendente: {lista}")

# Ordenar números enteros o coma flotante
numeros = [4,9,15,3,17,6,8, 3.14, 2.7172]
numeros.sort()
print(numeros)

# Ordenar datos booleanos
logica = [True, False, False, True, True]
logica.sort()
print(logica)