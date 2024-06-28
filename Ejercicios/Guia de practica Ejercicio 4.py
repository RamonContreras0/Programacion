''' 4. Crea un algoritmo que permita adivinar un número. En primer lugar el algoritmo debe solicitar un número entero por consola.
A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido.
El programa termina cuando se acierta el número.'''

def adivina_numero():
    # Solicitar al usuario que introduzca el número a adivinar
    numero_a_adivinar = int(input("Introduce el número a adivinar: "))

    print("Ahora, otro jugador debe adivinar el número.")

    # Bucle que continuará hasta que se adivine el número
    while True:
        # Solicitar al usuario que introduzca un número para adivinar
        intento = int(input("Introduce tu intento: "))

        # Comparar el número introducido con el número a adivinar
        if intento < numero_a_adivinar:
            print("El número es mayor que", intento)
        elif intento > numero_a_adivinar:
            print("El número es menor que", intento)
        else:
            print("¡Correcto! Has adivinado el número.")
            break

# Llamar a la función para iniciar el juego
adivina_numero()
