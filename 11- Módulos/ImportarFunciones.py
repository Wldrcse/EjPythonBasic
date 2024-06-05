# Importamos las funciones declaradas en el archivo areas.py
import areas

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
            areas.HallarAreaRectangulo()
        elif ( op == 2):
            areas.HallarAreaCuadrado()
        elif ( op == 3):
            areas.HallarAreaCirculo()
        elif ( op == 4):
            areas.HallarAreaTriangulo()
        else:
            print("Saliendo del sistema!")
            resp = False
    else:
        rp = input("No es una opción del menú, desea volver a intentarlo S/N: ")
        rp = rp.upper()
        if ( rp != 'S'):
            print("Saliendo del sistema!")
            resp = False