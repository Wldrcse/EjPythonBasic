# Total a pagar
precio = 150
desc = 0.1
print("Producto a comprar: Teclado Gamer")
print("Precio Catálogo:",precio)
print("Descuento:",(desc*100),"%")
num = int(input("Ingrese el número de unidades a comprar: "))
TotalPagar = num*precio - num*precio*desc
print("Total a pagar:",TotalPagar)
