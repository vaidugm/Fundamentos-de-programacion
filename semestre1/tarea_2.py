num = int(input("Ingresa un numero: "))

print (f"Intervalo de 1-25", 1 <= num <= 25)
print (f"Intervalo de 26-50", 26 <= num <= 50)
print (f"Intervalo de 51-75", 51 <= num <= 75)
print (f"Intervalo de 76-100", 76 <= num <= 100)
print (f"Fuera de rango", num < 1 or num > 100)