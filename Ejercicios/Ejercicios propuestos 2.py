
descrip_prod1 = input("Ingrese la descripción del producto 1: ")
precio_1 = int(input("Ingrese el precio en pesos chilenos del producto 1: "))
cantidad_1 = int(input("Ingrese la cantidad disponible del producto 1: "))

longitud1 = len(descrip_prod1) < 40

descrip_prod2 = input("\nIngrese la descripción del producto 2: ")
precio_2 = int(input("Ingrese el precio en pesos chilenos del producto 2: "))
cantidad_2 = int(input("Ingrese la cantidad disponible del producto 2: "))

longitud2 = len(descrip_prod2) < 40

descrip1_may = descrip_prod1.upper()
descrip2_may = descrip_prod2.upper()

# Unir con Espacios
newdescrip1 = ' '.join(descrip1_may.split())
newdescrip2 = ' '.join(descrip2_may.split())

v1 = precio_1 * cantidad_1
v2 = precio_2 * cantidad_2

print(f"\nDescripción Ingresada del producto 1: {descrip_prod1}")
print(f"¿El tamaño de la descripción es mayor a 40 caracteres? {longitud1}")
print(f"Descripción en mayúsculas del producto 1: {descrip1_may}")
print(f"Descripción unida con espacios del producto 1: {newdescrip1}")
print(f"Valor total del inventario para el producto 1: {v1} CLP")

print(f"\nDescripción Ingresada del producto 2: {descrip_prod2}")
print(f"¿El tamaño de la descripción es mayor a 40 caracteres? {longitud2}")
print(f"Descripción en mayúsculas del producto 2: {descrip2_may}")
print(f"Descripción unida con espacios del producto 2: {newdescrip2}")
print(f"Valor total del inventario para el producto 2: {v2} CLP")

valor_inventario = v1 + v2
precio_prom = ((precio_1 + precio_2)/2)

print(f"\nEl valor total del inventario es: {valor_inventario} CLP")
print(f"El precio promedio entre los productos: {precio_prom:.2f} CLP")
