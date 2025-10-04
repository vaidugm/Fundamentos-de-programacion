rows = int(input("Ingresa un numero: "))

for row in range(rows//2, rows, 2):
    for col in range(1, rows - row, 2):
        print(" ", end="")
    for col in range(1, row + 1):
        print("*", end="")
    for col in range(1, rows - row + 1):
        print(" ", end="")
    for col in range(1, row + 1):
        print("*", end="")
    print()

for row in range(rows, 0, -1):
    for col in range(rows - row):
        print(" ", end="")
    for col in range(2 * row - 1):
        print("*", end="")
    print()
