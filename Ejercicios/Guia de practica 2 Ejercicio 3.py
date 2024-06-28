#3. Escribir un programa que pida al usuario una cadena de texto y luego la invierta usando ciclos.

cadena = input("Ingrese una cadena de texto: ")
cadena_invertida = ""
for i in range(len(cadena) - 1, -1, -1):
    cadena_invertida += cadena[i]

print("La cadena invertida es:", cadena_invertida)
