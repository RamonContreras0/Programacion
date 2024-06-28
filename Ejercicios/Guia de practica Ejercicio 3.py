''' 4. Crea un algoritmo que permita adivinar un número. En primer lugar el algoritmo debe solicitar un número entero por consola.
A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido.
El programa termina cuando se acierta el número.'''

def n1():
    n1 = int(input("Introduce el número a adivinar: "))
    while True:
        n2 = int(input("Introduce el numero que creas que sea el anterior: "))
        if n2 < n1:
            print("El número es mayor que", n2)
        elif n2 > n1:
            print("El número es menor que", n2)
        else:
            print("Has adivinado el número.")
            break
n1()
