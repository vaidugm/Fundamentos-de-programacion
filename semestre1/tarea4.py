print ("~~~~~ Compra de galletas de mamunts ~~~~~")

#Entradas

precion_unitario = float(input("Precio unitario de un mamut (5): "))
cantidad = int(input("Cuantas galletas mamuts quieres comprar: "))
stock = int(input("Cuantos mamuts hay en el inventario: "))

#Operadores aritmeticos

subtotal = precion_unitario * cantidad
iva = subtotal * 0.16
total = subtotal + iva
restante = stock - cantidad
division = total / max(cantidad, 1)
division_entera = cantidad // 6
modulo = cantidad % 6

#Operadores relacionales

alcanza_stock =  cantidad <= stock
compra_grande = total >= 500
mamut_caro = precion_unitario > 20
exacto_stock = cantidad == stock
ninguna = stock != 0

print ("\n --- Resultados ---") 
print (f"subtotal $ {cantidad:.2f}") 
print (f"IVA $ {iva:.2f}") 
print (f"Total $ {total:.2f}") 
print (f"Mamuts que quedan en inventario: {restante}")
print (f"Precio promedio por Mamut: {division:.2f}")
print (f"Cajas completas {division_entera}")
print (f"Sobrante fuera de caja {modulo}")
print( f"La cantidad alcanza con lo del inventario: {alcanza_stock}")
print( f"Es una compra grande: {compra_grande}")
print( f"El mamut esta caro: {mamut_caro}")
print( f"Lo comprada es igual ala del inventario: {exacto_stock}")
print( f"Se quedo vacion el inventario: {ninguna}")