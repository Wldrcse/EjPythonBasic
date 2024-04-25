PrecioP1 = float(input("Ingrese precio del producto 1: "))
PrecioP2 = float(input("Ingrese precio del producto 2: "))
cant1 = int(input("Ingrese número de productos a comprar del Producto 1: "))
cant2 = int(input("Ingrese número de productos a comprar del Producto 2: "))
desc = float(input("Descuento a aplicar: "))
total = PrecioP1 * cant1 + PrecioP2 * cant2
totalPagar = total - total*desc/100
print(f"Total a Pagar: S/ {totalPagar}")
