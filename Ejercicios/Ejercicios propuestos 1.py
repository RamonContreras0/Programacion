descripcion = "Este lapiz azul es de tinta"


descripcion = descripcion[:50]


longitud = len(descripcion) > 50 
print(type(longitud))


descrip_10 = descripcion[:10]

print(f"\nDescripción: {descripcion}")
print(f"¿El tamaño de la cadena descripción es mayor a 50 caracteres? {longitud}")
print(f"Los primeros 10 caracteres de la descripción: {descrip_10}")
