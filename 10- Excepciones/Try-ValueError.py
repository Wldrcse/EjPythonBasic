# try:
	# Codigo a ejecutar
	# Pero podria haber errores en este bloque
    
# except <tipo de error>:
	# Haz esto para manejar la excepcion
	# El bloque except se ejecutara si el bloque try lanza un error
    
# else:
	# Esto se ejecutara si el bloque try se ejecuta sin errores
   
# finally:
	# Este bloque se ejecutara siempre

'''
Tipos de excepciones
Los principales excepciones definidas en Python son:

TypeError : Ocurre cuando se aplica una operación o función a un dato del tipo inapropiado.
ZeroDivisionError : Ocurre cuando se itenta dividir por cero.
OverflowError : Ocurre cuando un cálculo excede el límite para un tipo de dato numérico.
IndexError : Ocurre cuando se intenta acceder a una secuencia con un índice que no existe.
KeyError : Ocurre cuando se intenta acceder a un diccionario con una clave que no existe.
FileNotFoundError : Ocurre cuando se intenta acceder a un fichero que no existe en la ruta indicada.
ImportError : Ocurre cuando falla la importación de un módulo. '''

while True:
    try:
        n = int(input("Ingrese un número entero: "))
        print(f"El número ingresado es un entero igual a {n}")
        break
    except ValueError:
        print("No es un número entero")

while True:
    try:
        m = int(input("Ingrese un número entero: "))
    except ValueError:
        print("No es un número entero")
    else:
        print(f"El número ingresado es un entero igual a {m}")
        break
while True:
    try:
        t = int(input("Ingrese un número entero: "))
    except ValueError:
        print("No es un número entero")
    else:
        print(f"El número ingresado es un entero igual a {t}")
        break
    finally:
        print("Fín del programa")


#    modulos
