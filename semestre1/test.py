saldo = 100

print("Bienvenido al sistema de retiros.")
print(f"Saldo disponible: ${saldo:.2f}\n")

while saldo > 0:
    retiro = float(input("¿Cuanto deseas retirar?: "))

    if retiro > saldo:
        print(f"No tienes saldo suficiente")
        break
    else:
        saldo -= retiro
        print(f"Has retirado ${retiro:.2f}. Saldo restante: ${saldo:.2f}\n")

print("Saldo agotado. No puedes hacer mas retiros.")

