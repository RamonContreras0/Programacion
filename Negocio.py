"""Un negocio quiere organizar sus productos por fecha de vencimiento. Desarrollar un
programa que permita ingresar las fechas de vencimiento (día, mes, año) de tres productos
y almacenarlas en tuplas. Luego, mostrar las fechas ordenadas de menor a mayor.
a. Ingresar las fechas de vencimiento (día, mes, año) de tres productos por consola, y
almacenarlas en tuplas.
b. Ordenar las fechas de menor a mayor utilizando la función correspondiente de
Python.
c. Mostrar las fechas ordenadas."""

producto1 = input("Ingrese el nombre del primer producto ")
producto2 = input("Ingrese el nombre del segundo producto ")
producto3 = input("Ingrese el nombre del tercer producto ")
fecha1 = (input("Ingrese el dia "), input("mes "), input("y año de la fecha de vencimiento "))
fecha2 = (input("Ingrese el dia "), input("mes "), input("y año de la fecha de vencimiento "))
fecha3 = (input("Ingrese el dia "), input("mes "), input("y año de la fecha de vencimiento "))
fechas = tuple()
fechas = fecha1, fecha2, fecha3
print(fechas)
fechas = sorted([fecha1, fecha2, fecha3])
print(fechas)