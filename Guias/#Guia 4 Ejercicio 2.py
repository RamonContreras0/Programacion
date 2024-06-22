#Guia 4 Ejercicio 2
#Construir un programa permita calcular e imprimir el resultado de la siguiente sumatoria:
#S = 500 + 456 + 510 + 454 + 520 + 452 + ... + 800 

def resultado():
 
    suma = 0
    a = 500
    b = 456

    while a <= 800:
        suma += a
        suma += b
        a += 10
        b -= 2
    return suma
n = resultado()
print(f"El resultado es: {n}")
