# Total a pagar
precio = 150.00
desc = 0.1
print("Producto a comprar: Teclado Gamer")
print(f"Precio Catálogo: S/ {precio:.2f}")
# print(f"Precio catálogo: {precio}")
#print("Descuento:",(desc*100),"%")
print(f"Descuento {desc*100}%")
num = int(input("Ingrese el número de unidades a comprar: "))
TotalPagar = num*precio - num*precio*desc
print(f"Total descuento: S/ {(desc*num*precio):.2f}")
print(f"Total a pagar: S/ {TotalPagar:.2f}")
