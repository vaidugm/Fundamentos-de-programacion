cadena = input("Ingrese una oracion: ")

contador = 0
vocales = ("aeiouAEIOU")

for x in cadena:
    if  x in vocales:
        contador += 1
print("El numero de vocales que contiene la oracion ingresada es: ", contador)