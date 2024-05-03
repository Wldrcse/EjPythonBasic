def ContarDigitos(num):
    numStr = str(num)
    numDigitos = len(numStr)
    print(f"EL número {numStr} tiene {numDigitos} dígitos")
    
continuar = True
while (continuar):
    print('\nContar cantidad de dígitos de un número')        
    n = int(input("Ingrese un número: "))
    ContarDigitos(n)
    rp = input("¿Desea volver a ejecutar S/N?: ")
    rp = rp.upper()
    if ( rp != 'S' ):
        continuar = False