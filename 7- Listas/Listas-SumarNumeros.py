lista = []
n = int(input("Cuantos números desea ingresar?: "))
suma = 0
for i in range (n):
    temp = int(input(f"Ingrese número {i+1}: "))
    lista.append(temp)
    suma = suma + temp
print(f"Los números ingresados son: {lista}")
print(f"La suma de los números ingresados es: {suma}")
print(f"El promedio de los números ingresados es: {suma/n:.2f}")
eliminar = int(input("Ingrese el número a eliminar: "))
for i in range(n):
    if ( eliminar == lista[i] ):
        print(f"Valor encontrado, se procederá a eliminar!")
        lista.remove(eliminar)
        suma = suma - eliminar
        print(f"Números ingresados: {lista}")
        print(f"La suma de los números ingresados es: {suma}")
        print(f"El promedio de los números ingresados es: {suma/len(lista):.2f}")
        break
else:
    print("Error, número no encontrado!")


