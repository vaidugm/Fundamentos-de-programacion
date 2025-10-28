def menu():
    while True:
        print ("~~~Que opcion deseas realizar~~~")
        print ("Perimetro del Cuadrado (1)")
        print ("Perimetro del Rectangulo (2)")
        print ("Cerrar programa (3)")

        n = input("Ingresa el numero de la opcion que deseas: ")   

        if n == "1":
            lado = float(input("Ingresa la medida del lado del cuadrado: "))
            print(f"El perimetro del cuadrado es: {4 * lado}\n")
        elif n == "2":
            largo = float(input("Ingresa la medida del largo del rectangulo: "))
            ancho = float(input("Ingresa la medida del ancho del rectangulo: "))
            print(f"El perimetro del rectangulo es: {2 * (largo + ancho)}\n")
        elif n == "3":
            break
        else:
            print("Opcion no valida. Por favor, intenta de nuevo.\n")
menu()
