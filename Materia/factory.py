def factorial(num):
    print("Valor inicial ->", num)
    if num > 1:
        num = num * factorial(num -1)
    print("Valor final ->",num)
    return num

print(factorial(5))

def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Juan")  # Aquí "Juan" es un argumento

def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(resultado)  # Imprimirá 8

def multiplicar(x, y, z):
    return x * y * z

resultado = multiplicar(2, 3, 4)
print(resultado)  # Imprimirá 24

def calcular_area_circulo(radio, pi=3.14):
    return pi * radio * radio

area = calcular_area_circulo(5)
print(f"El área del círculo es: {area}")

