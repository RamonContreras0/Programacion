'''1. Se cuenta con tres tuplas: la primera contiene los puntajes más altos obtenidos por estudiantes en Matemáticas.
La segunda tupla contiene los puntajes más altos en Química.
Por último, la tercera tupla contiene los puntajes más altos en Programación.
● Puntajes Matemáticas = (55, 17, 93, 75, 88, 55)
● Puntajes Química = (10, 85, 75, 88, 91, 75)
● Puntajes Programación = (68, 78, 85, 68, 82, 10)
A) Imprimir los valores duplicados de cada tupla
B) Convertir cada tupla en una lista y ordenar las listas en orden descendente.
C) Unir las listas anteriormente generadas en una sola y eliminar los duplicados.
D) Encontrar el puntaje máximo y mínimo de la lista resultante.'''

puntajes_matematicas = (55, 17, 93, 75, 88, 55)
puntajes_quimica = (10, 85, 75, 88, 91, 75)
puntajes_programacion = (68, 78, 85, 68, 82, 10)

from collections import Counter
def numeros_duplicados(tupla):
    contador = Counter(tupla)
    duplicados = [item for item, count in contador.items() if count > 1]
    return duplicados

duplicados_matematicas = numeros_duplicados(puntajes_matematicas)
duplicados_quimica = numeros_duplicados(puntajes_quimica)
duplicados_programacion = numeros_duplicados(puntajes_programacion)

print("Numeros repetidos en Matemáticas:", duplicados_matematicas)
print("Numeros repetidos en Química:", duplicados_quimica)
print("Numeros repetidos en Programación:", duplicados_programacion)

lista_matematicas = sorted(list(puntajes_matematicas), reverse=True)
lista_quimica = sorted(list(puntajes_quimica), reverse=True)
lista_programacion = sorted(list(puntajes_programacion), reverse=True)

print("Lista de Matemáticas ordenada:", lista_matematicas)
print("Lista de Química ordenada:", lista_quimica)
print("Lista de Programación ordenada:", lista_programacion)

lista_total = lista_matematicas + lista_quimica + lista_programacion
lista_final = list(set(lista_total))

print("Lista unida sin duplicados:", lista_final)

# D) Encontrar el puntaje máximo y mínimo
puntaje_maximo = max(lista_final)
puntaje_minimo = min(lista_final)

print("Puntaje máximo:", puntaje_maximo)
print("Puntaje mínimo:", puntaje_minimo)
