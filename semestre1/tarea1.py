print( "~~~~Que deseas realizar~~~~" )
print( "1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir" )

problema = int(input("Elije la opcion a realizar: "))

num1 = int(input ( "Ingresa un numero: " ) )
num2 = int(input ( "Ingresa un numero: " ) )

if problema == 1:
    print ( "La solucion a tu suma es: ", num1 + num2 )    
elif problema == 2:
    print ( "La solucion a tu resta es: ", num1 - num2 )
elif problema == 3:
    print ( "La solucion a tu multiplicacion es: ", num1 * num2 )
elif problema == 4:
    print ( "La solucion a tu division es: ", num1 / num2 )
