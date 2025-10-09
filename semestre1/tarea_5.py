#ejercicio 1
total= 0

print("Escribe 'fin' para terminar.")

while True:
    monto = input("Ingrese el monto de la venta: ")
    
    if monto.lower() == "fin":
        break 
    
    total += float(monto)

print(f"El total acumulado de ventas es: ${total:.2f}")

#ejercicio 2
total = 0

print("Escribe 'fin' para terminar.")

while True:
    entrada = input("Ingrese las horas que estuvo estacionado el auto: ")

    if entrada.lower() == "fin":
        break

    horas = float(entrada)

    cobro = horas * 3

    total += cobro

    print(f"Cobro por este auto: ${cobro:.2f}")
   
print(f"\nTotal cobrado por todos los autos: ${total:.2f}")

#ejercicio 3
saldo = 100

print("Bienvenido al sistema de retiros.")
print(f"Saldo disponible: ${saldo:.2f}\n")

while saldo > 0:
    retiro = float(input("¿Cuanto deseas retirar?: "))

    saldo -= retiro
    print(f"Has retirado ${retiro:.2f}. Saldo restante: ${saldo:.2f}\n")

print("Saldo agotado.")

