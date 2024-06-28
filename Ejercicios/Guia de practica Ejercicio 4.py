''' 4. Crea un algoritmo que permita adivinar un número. En primer lugar el algoritmo debe solicitar un número entero por consola.
A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido.
El programa termina cuando se acierta el número.'''

def adivina_numero():
    numero_a_adivinar = int(input("Introduce un número: "))
    while True:
        intento = int(input("Introduce el numero que creas correcto:"))
        if intento < numero_a_adivinar:
            print("El número es mayor que", intento)
        elif intento > numero_a_adivinar:
            print("El número es menor que", intento)
        else:
            print("Has adivinado el número.")
            break
adivina_numero()
