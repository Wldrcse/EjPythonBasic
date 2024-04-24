# Declaramos funciones
def Lunes():
    print("Día Lunes")
def Martes():
    print("Día Martes")
def Miércoles():
    print("Día Miércoles")
def Jueves():
    print("Día Jueves")
def Viernes():
    print("Día Viernes")
def Sábado():
    print("Día Sábado")
def Domingo():
    print("Día Domingo")
# Solicitamos pueda ingresar un número
dia = int(input("Ingrese un día de la semana: "))
switch_dia ={
    1: Lunes,
    2: Martes,
    3: Miércoles,
    4: Jueves,
    5: Viernes,
    6: Sábado,
    7: Domingo
}

# Invocamos a la función
switch_dia.get(dia)()


