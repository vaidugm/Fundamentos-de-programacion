'''

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un numero: "))

print ( "Resultado: ", num1 + num2 )

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un numero: "))

print ( "Resultado: ", num1 - num2 )

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un numero: "))

print ( "Resultado: ", num1 * num2 )

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un numero: "))

print ( "Resultado: ", num1 / num2 )
'''
# Funciones para cada operación
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida."

# Función principal de la calculadora
def calculadora():
    print("Bienvenido a la calculadora.")
    
    while True:
        # Menú de opciones
        print("\nElige una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        try:
            opcion = int(input("Ingresa el número de la operación: "))
            
            if opcion == 5:
                print("Gracias por usar la calculadora.")
                break
            
            if opcion not in [1, 2, 3, 4]:
                print("Opción no válida. Intenta de nuevo.")
                continue
            
            # Solicitar los números para operar
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            
            # Realizar la operación según la opción elegida
            if opcion == 1:
                resultado = sumar(num1, num2)
                print(f"El resultado de {num1} + {num2} es: {resultado}")
            elif opcion == 2:
                resultado = restar(num1, num2)
                print(f"El resultado de {num1} - {num2} es: {resultado}")
            elif opcion == 3:
                resultado = multiplicar(num1, num2)
                print(f"El resultado de {num1} * {num2} es: {resultado}")
            elif opcion == 4:
                resultado = dividir(num1, num2)
                print(f"El resultado de {num1} / {num2} es: {resultado}")
            
        except ValueError:
            print("Entrada no válida. Por favor, ingresa números válidos.")
        
# Llamar la función para iniciar la calculadora
calculadora()
