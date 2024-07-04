# Ejercicio: Crear el Script que permita agregar los 3 primeros días de la semana, luego agregará un solo elemento más el cual será el día jueves, después agregará el resto de días en conjunto, con esto mostrará los siguientes datos:
# Indicar el número de elementos de la lista
# Imprimir todos los elementos de la lista
# Imprimir solo los 3 primeros elementos
# Imprimir desde el índice 2 al índice 4
# Imprimir el penúltimo elemento de la lista
# ordenar los elementos de la lista de manera descendente

dias_Semana = ["Lunes", "Martes", "Miércoles"]
print(f"Días de la semana: {dias_Semana}")
dias_Semana.append("Jueves")
print(f"Días de la semana: {dias_Semana}")
dias_Semana.extend(["Viernes", "Sábado", "Domingo"])
print(f"Días de la semana: {dias_Semana}")
print(f"Número de elementos de la lista: {len(dias_Semana)}")
print(f"Todos los elementos de la lista: {dias_Semana}")
print(f"3 primeros elementos de la lista: {dias_Semana[0:3]}")
print(f"Imprimir desde el índice 2 al índice 4: {dias_Semana[2:5]}")
print(f"Penúltimo elemento de la lista: {dias_Semana[-2]}")
dias_Semana.sort(reverse=True)
print(f"Lista ordenada de manera descendente: {dias_Semana}")


