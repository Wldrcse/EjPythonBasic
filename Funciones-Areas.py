def FARectangulo(): # Función para calcular el área de un Rectángulo
    print('''** Área del Rectángulo  **
          
    ****************
    *              *
    *              *  Lado menor
    *              *
    ****************
       Lado mayor''')
    lma = float(input("Ingrese el lado mayor: "))
    lme = float(input("Ingrese el lado menor: "))
    AreaRec = lma * lme
    print(f"El área del rectángulo es {AreaRec:.2f}")

def FACuadrado(): # Función para calcular el área de un Cuadrado
    print('''** Área del Cuadrado  **
          
    ************
    *          *
    *          *  Lado
    *          *
    ************
       Lado''')
    lado = float(input("Ingrese el lado del cuadrado: "))
    AreaC = lado**2
    print(f"El área del cuadrado es {AreaC:.2f}")

def FACirculo(): # Función para calcular el área de un círculo
    print('''** Área del Círculo  **
              _
           *     *
        *           *
      *          r    *
     |        -------> |
      *               *
        *           *
           *  _  *''')
    radio = float(input("Ingrese el radio del círculo: "))
    pi = 3.14
    AreaCir = pi*(radio**2)
    print(f"El área del círculo es {AreaCir:.2f}")
    
def FATriangulo(): # Función para calcular el área de un triángulo
    print('''** Área del Triángulo  **
          
        *
         *  *
          *    *
    Altura *       *
            *          *
             *              *
              *****************     
                    Base''')
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    AreaTri = base * altura
    print(f"El área del círculo es {AreaTri:.2f}")

def Salir(): # Función para salir del sistema
    rp = input("Desea volver al menú principal S/N?: ")
    rp = rp.upper()
    if ( rp != 'S' ):
        return False
    else:
        return True
    
resp = True
while(resp):
    # Menú de Opciones
    menu = '''**  Cálculo de Áreas  **
    1- Área del Rectángulo
    2- Área del Cuadrado
    3- Área del Círculo
    4- Área del Triángulo
    5- Salir'''
    print(menu)
    op = int(input("Ingrese una opción: "))
    if ( op >= 1 and op <= 5 ):
        if ( op == 1):
            FARectangulo()
            resp = Salir()
        elif ( op == 2):
            FACuadrado()
            resp = Salir()
        elif ( op == 3):
            FACirculo()
            resp = Salir()
        elif ( op == 4):
            FATriangulo()
            resp = Salir()
        else:
            print("Saliendo del sistema!")
            resp = False
    else:
        rp = input("No es una opción del menú, desea volver a intentarlo S/N: ")
        rp = rp.upper()
        if ( rp != 'S'):
            print("Saliendo del sistema!")
            resp = False