'''Una editorial digital quiere desarrollar una aplicación para gestionar y manipular el
contenido de los artículos que publican. Es por esto, que se debe crear un módulo que
permita realizar diversas operaciones con cadenas de texto para analizar y modificar los
artículos de manera eficiente. (50 Puntos)
Se solicita:
1. Ingresar un breve resumen del artículo igual o menor a 60 caracteres. Solicitar este
breve resumen por terminal.
2. Crear una variable booleana que almacene True si la longitud de la variable que
almacena el resumen es igual o menor a 60 caracteres y False en caso contrario.
3. Mostrar en pantalla las siguientes operaciones:
a. Imprimir la longitud de caracteres del breve resumen del artículo.
b. Convertir el resumen en mayúsculas utilizando la función de Python adecuada.
c. Mostrar los últimos diez caracteres del resumen.
d. Unir las palabras del resumen con un guión (-) como separador utilizando la función correcta.'''


descripción = input("Ingrese una descripción del articulo de menos de 60 caracteres: ")

descripción2 = len(descripción) <= 60
print(f"Descripcion menor o igual a 60 = {descripción2}")
print(f"La cantidad de caracteres que tiene la descripción es de  {len(descripción)}")

Mayus= descripción.upper()
print(f"La descripcion en mayúsculas es : {Mayus}")

ultimos10 = descripción[-10:]
print (" Los ultimos 10 caracteres son: ", ultimos10)

separados = (descripción.split())
unidos = '-'.join(separados)
print(f"Las palabras del resumen son:{unidos}")