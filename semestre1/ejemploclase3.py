n = int(input("Cuantos objetos requieres agreggar: "))

productos = []
precios = []

total = 0
for i in range(n):
    producto = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    productos.append(producto)
    precios.append(precio)

    total += precios[i]

print(f"\n{'Producto':<20}{'Precio':>10}")
print("-" * 30)

for producto, precio in zip(productos, precios):
    print(f"{producto:<20}{precio:>10.2f}")

if (total > 500):
    descuento = total * 0.10
    total -= descuento
    print(f"\nDescuento aplicado: {descuento:.2f}")
