
#1 Operadores aritmeticos
a = 20
b = 5
c = 4
d = 20

#Operaciones comunes

print("Suma entre a + b es:", a + b)
print("Resta entre a - b es:", a - b)
print("Multiplicacion entre a * b es:", a * b)
print("Division entre a / b es:", a / b)
print("El modulo entre a y b es:", a % b)
print("El cosiente entre b / c:", b // c)
print("El resultado de b elevado a c es:", b**c)

#declarando variantes en tipo flotantes

t = 5.39 #Tiempo en segundos
g = 9.81 #La aceleracion de gravedad
v = 8
print(f"la velocidad del objeto en caida libre es de {v} m/s")
print("La velocidad del objeto en caida libre es de: {:.2f}".format(v))
print("\n")

#Declarando varible tipo compleja
c1 = 4 + 3j
print(type(c1))
#Declarando complejo con complex
c2 = complex(3,- 5)
print("El numero complejo es:" ,c2)

print(c2.real) #Opteniendo partee real del numero complejo
print(c2.imag) #Obteniendo la parte imaginaroa del numero complejo

print("Hola" * 5)
print("Hola" * (int((10 * 2) /5)), "\n")

#2 Operadores de Comparacion
print(a == b) #Igual a
print(a != b) #Distinto a
print(a > b) #Mayor que
print(a < b) #Menor que
print(c >= d) #Mayor o igual que 
print(c <= d) #Menor o igual que

#Comparando cadenas de caracteres
animal_domestico = "Gato"
animal_salvaje = "Leopardo"
print(animal_domestico == animal_salvaje)
print(animal_domestico != animal_salvaje)
print(animal_domestico > animal_salvaje)
print(animal_domestico < animal_salvaje)
print(animal_domestico >= animal_salvaje)
print(animal_domestico <= animal_salvaje)

#3 Operaciones Logicos

bencina = True
encendido = True
edad = 19

#Utilizando el operador AND
if bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede avanzar")

#Utilizando el operador OR
if bencina or encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede avanzar")

#Utilizando el operador NOT junto al AND
if not bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede avanzar")

