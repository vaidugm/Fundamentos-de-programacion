#1. Numeros pares e impares
num = int(input("Ingresa un numero entero: "))

if num % 2 == 0:
    print("Es un numero par" ,  num % 2 == 0)
else :
    print("Es impar")

#2. Calculadora simple

print( "~~~~Que deseas realizar~~~~" )
print( "1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir" )

problema = int(input("Que opcion deseas realizar (1..4): "))

num1 = int(input ( "Ingresa el primer numero: " ) )
num2 = int(input ( "Ingresa el segundo numero: " ) )

if problema == 1:
    print ( f"La solucion a tu suma es: {num1 + num2}" )    
elif problema == 2:
    print ( f"La solucion a tu resta es: {num1 - num2}" )
elif problema == 3:
    print ( f"La solucion a tu multiplicacion es: {num1 * num2}" )
elif problema == 4:
    print ( f"La solucion a tu division es: {num1 / num2}" )

#3.Clasificación de edades

edad = int(input("Ingresa tu edad: "))

if edad < 18:
    print( f"Tu edad es {edad}, eres menor de edad" )
elif 18 >= edad <= 59:
   print( f"Tu edad es {edad}, eres mayor de edad" )
else:
    print( f"Tu edad es {edad}, eres un adulto mayor" )

#4. Tabla de multiplicar con for
numero = int(input("Ingresa un numero: "))

print(f"\nTabla de multiplicar del {numero}:\n")
for i in range(1, 11): 
    print(f"{numero} x {i} = {numero * i}")

#5. Adivina el número 
for intento in range(1, 4):
    numero = int(input(" Ingresa tu numero: "))

    if numero == 2:
        print("Adivinaste el numero")
        break
    else:
        print("Ese no es el numero")
        if intento < 3:
            print("Vuelve a intentar")
else:
    print("Fallaste el numero era 2")

#6. Claificaciones de alumnos

#7. Contador de vocales
cadena = input("Ingrese una oracion: ")

contador = 0
vocales = ("aeiouAEIOU")

for x in cadena:
    if  x in vocales:
        contador += 1
print("El numero de vocales que contiene la oracion ingresada es: ", contador)

#8. Validación de contraseña
texto = input("Ingresa la contraseña: ")

if texto == "python123":
    print ("Contraseña correcta")
else:
    print ("Contraseña incorrecta")