import time

class Color:
    RED = '\x1b[0;31;50m'
    BOLD_RED = '\x1b[1;31;50m'
    NORMAL = '\x1b[0m'

def cargar_corazon():
    with open('Fundamentos-de-programacion/resources/heart_pattern.txt', 'r') as f:
        return f.read()

def romantizar(nombre):
    corazon = cargar_corazon()
    letras = list(nombre)
    i = 0
    while '@' in corazon:
        corazon = corazon.replace('@', letras[i % len(letras)], 1)
        i += 1
    return corazon

def main():
    nombre = input("Ingresa un nombre: ").strip() or "Amor"
    corazon = romantizar(nombre)
    
    print(f"\n{Color.BOLD_RED}♥ Formando corazon... ♥{Color.NORMAL}\n")
    time.sleep(1)
    for linea in corazon.split('\n'):
        if linea.strip():
            print(f"{Color.RED}{linea}{Color.NORMAL}")
            time.sleep(0.3)
    
    print(f"\n{Color.BOLD_RED}Te queyo, {nombre}! ♥{Color.NORMAL}")

if __name__ == '__main__':
    main()