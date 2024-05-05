lenguajes = ('Python', 'Php', 'Java', 'R', 'C++', 'Python')

# Index() Este método recibe un elemento como argumento, y devuelve el índice de su primera aparición en la tupla.
print(f"Mostrar el índice de Python: {lenguajes.index('Python')}")

# Len() Este método permite indicar la longitud de la tupla.
print(f"Longitud de la tupla: {len(lenguajes)}")

# Count() Permite consultar cuántas veces aparece un elemento dentro de una tupla 
print(f"El texto Python se repite {lenguajes.count('Python')} veces en la tupla")

# Len() Permite indicar la cantidad de elementos de la tupla
print(f"Total de elementos de la tupla: {len(lenguajes)}")

# Del() Permite eliminar la tupla
del(lenguajes)
# Esto produce error
# print(f"Tipo de dato almacenado en lenguaje: {type(lenguajes)}")