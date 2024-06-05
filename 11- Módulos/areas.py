def HallarAreaRectangulo(): # Función para calcular el área de un Rectángulo
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

def HallarAreaCuadrado(): # Función para calcular el área de un Cuadrado
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

def HallarAreaCirculo(): # Función para calcular el área de un círculo
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
    
def HallarAreaTriangulo(): # Función para calcular el área de un triángulo
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