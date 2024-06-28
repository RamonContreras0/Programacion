""" Crear un programa que permita ingresar 4 marcas de bebidas gaseosas y almacenarlas en una lista. Luego, mostrar la lista completa y el nombre de la primera y última bebida.
a. Ingresar 4 nombres de marcas de bebida por consola y almacenarlos en una lista.
b. Imprimir la lista completa.
c. Mostrar el primer y último nombre de las bebidas de la lista."""

marca1 = input("Ingrese la primera marca de bebidas ")
marca2 = input("Ingrese la segunda marca de bebidas ")
marca3 = input("Ingrese la tercera marca de bebidas ")
marca4 = input("Ingrese la cuarta marca de bebidas ")

marcas = [marca1, marca2, marca3, marca4]
print("Las cuatro marcas son :", marcas)
print("La primera y utima marca son: ", marcas[0], marcas[3])
