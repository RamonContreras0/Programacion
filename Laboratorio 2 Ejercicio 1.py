Manzana = 100# Valor unitario de las manzanas
CantidadM = 150# Cantidad de manzanas
Pera = 250# Valor unitario de las peras
CantidadP = 80# Cantidad de peras
Durazno = 300# Valor unitario de los duraznos
CantidadD = 120# Cantidad de duraznos
ValorM = Manzana * CantidadM #Multiplicar el valor de las manzanas por la cantidad de estas
ValorP = Pera * CantidadP#Multiplicar el valor de las peras por la cantidad de estas
ValorD = Durazno * CantidadD#Multiplicar el valor de los duraznos por la cantidad de estas
print("El total a pagar por las manzanas es de ", ValorM)
print("El total a pagar por las peras es de ", ValorP)
print("El total a pagar por las duraznos es de ", ValorD)

ValorMaximo = max(ValorM, ValorD, ValorP)# Calcular el valor mas alto
print("El valor mas alto a pagar es de ", ValorMaximo)

ValorMinimo = min(ValorM, ValorP, ValorD)# Calcular el valor mas bajo
print("El valor mas bajo a pagar es de ", ValorMinimo)

Promedio = (Durazno + Pera + Manzana)/3 # Calcular el promedio el valor unitario
print("El promedio a pagar entre las tres frutas es de ", Promedio)