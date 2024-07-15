'''
2. Determinar si una palabra ingresada por teclado es un palíndromo. Eliminar espacios y
convertir el texto ingresado a minúsculas. Además, imprimir la palabra invertida. (40 Puntos)
Un palíndromo es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda
Ejemplos:
● Oso
● "Sometamos o matemos"
● "Isaac no ronca así"
● Radar
● Ana
'''
palabra = input("Ingrese un palindro: ")
palabra = palabra.lower()
palabra = palabra.split()

print(palabra)