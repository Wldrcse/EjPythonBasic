# --> Métodos de los diccionarios
dic_alumno = {"ID": 1, "Nombre": "Luis", "Apellido": "Torres", "Especialidad": "Ing. de Software"}

# Len() Este método permite indicar la longitud del diccionario.
longitud =len(dic_alumno)
print(f"Diccionario: {dic_alumno}")
print(f"Longitud: {longitud}")

#  Del() Permite Eliminar claves y valores de los Diccionarios
print(f"Diccionario Original:{dic_alumno}")
del (dic_alumno['Especialidad'])
print(f"Diccionario modificado:{dic_alumno}")

# Pop() Permite Eliminar claves y valores de los Diccionarios
print(f"Diccionario Original: {dic_alumno}")
dic_alumno.pop('ID')
print(f"Diccionario modificado: {dic_alumno}")

# Popitem() Permite eliminar de manera aleatoria un elemento del diccionario.
print(f"Diccionario Original: {dic_alumno}")
dic_alumno.popitem()
print(f"Diccionario modificado: {dic_alumno}")

# Update() se llama sobre un diccionario y tiene como entrada
# otro diccionario. Los value son actualizados y
# si alguna key del nuevo diccionario no esta, es añadida.
dic_alumno1 = {"ID": 0,"Nombre": "André", "Apellido": "Gonzáles"}
dic_alumno_modif = {"ID": 5,"Dirección":"Jr. Sal y Rosas N 123","País":'Perú'}

# Actualizamos el diccionario con elementos del otro diccionario
dic_alumno1.update(dic_alumno_modif)
print(f"Diccionario modificado: {dic_alumno1}")

# Clear() Permite Eliminar todos los elementos de los Diccionarios
print(f"Diccionario Original: {dic_alumno1}")
dic_alumno1.clear()
print(f"Diccionario vacío: {dic_alumno1}")
