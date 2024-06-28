'''Desarrollar un algoritmo que permita devolver la siguiente propiedad descubierta por Nicomaco de Gerasa:
Sumando el primer impar, se obtiene el primer cubo.
Sumando los dos siguientes impares, se obtiene el segundo cubo
Sumando los tres siguientes, se obtiene el tercer cubo, y así sucesivamente.
Ejemplo:
1
3 = 1 = 1
2
3 = 3 + 5 = 8
3
3 = 7 + 9 + 11 = 27
4
3 = 13 + 15 + 17 + 19 = 64
Imprimir por pantalla, los primeros n cubos, considerando el valor de n obtenido desde teclado'''

n = int(input("Ingrese un numero "))
n_impar = (n*(n-1)) + 1
n2 = 0
for i in range(n):
    n2= n2 + n_impar
    if i == (n * 1):
        break
    n_impar = n_impar +2
    print(n_impar)

print(f"El cubo del numero es: {n2}")