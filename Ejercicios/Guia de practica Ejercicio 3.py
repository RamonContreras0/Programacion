#3. Ingresar 150 caracteres e indicar cuantas veces se repite el carácter ‘a’
cadena = input("Ingrese una cadena de 150 caracteres: ")
while len(cadena) != 150:
    cadena = input("La cadena no tiene exactamente 150 caracteres. Por favor, ingrese una cadena de 150 caracteres: ")
a = cadena.count('a')
print(f"El carácter 'a' se repite {a} veces en la cadena ingresada.")
