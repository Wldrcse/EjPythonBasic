# *********** DICCIONARIOS ***********

# Para declara un diccionario utilizamos Llaves, dos puntos y separador comas
d1 = {"ID": 1,"Nombre": "Luis", "Apellido": "Torres"}
print(f"Diccionario: {d1}")

# Se puede crear un diccionario usando dict()
d2 = dict([("ID",2),("Nombre","Juan"),("Apellido","León")])
print(f"Diccionario: {d2}")

# También es posible usar el constructor dict() para crear un diccionario.
d3 = dict(ID=3,Nombre='Luciano',Apellido='Victorio')
print(f"Diccionario: {d3}")

# Podemos imprimir solo las llaves
print("Llaves del Diccionario")
for i in d3.keys():
    print(i)

# Podemos imprimir solo los valores
print("Valores del Diccionario")
for i in d3.values():
    print(i)

# Podemos imprimir tanto llaves como valores
for i,j in d3.items():
    print(f"Llave:{i} Valor:{j}")

# Imprimir el valor de una llave
print(f"Valor de la llave Nombre: {d3['Nombre']}")

# Modificar valores de los Diccionarios
# Para poder realizar esto debemos de utilizar:
d4 = {"ID": 1,"Nombre": "Luis", "Apellido": "Torres"}
print(f"Diccionario declarado: {d4}")
d4['ID']=4
print(f"Diccionario modificado: {d4}")

# Agregar elementos a un diccionario
d4['Especialidad']='Ingeniería de Software'
print(f"Diccionario modificado: {d4}")

# Ejercicios