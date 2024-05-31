# Este es un Hola Mundo
print("Hola Mundo")

"""Este es un
comentario multilinea"""

name = "Ramon"
print("Hola mi nombre es", name)

import math
estatura = 1.70
peso = 70

imc =peso/(estatura ** 2)
print(math.trunc(imc))


cuidades ="Castro","Queilen", "Ancud", "Castro", "Quellon", "Quemchi"
cuidades = list(cuidades)
print(len(cuidades))
cuidades[0] = "Quemchi" #reasignacion de valores
print(cuidades)

listnum = [1,2,3,4,5,6,7,8,9,10]
listnum2 = list(range(1,1001,10))
print(listnum2)


musica = tuple()
generos = ("Rock", "Blues", "Pop", "Trap", "HipHop")
print(generos)
print(type(generos))
print(generos.index("Pop"))

tuplita = ("Victor", 200, "Universidad", True)
print(tuplita)
tuplita = list(tuplita)
print("La tupla ahora es de tipo", type(tuplita))
#tomando un trozo de tupla
print(tuplita[0:3])

#6. SETS (conjuntos)
conjunto_vacio = set() # inicializar un set
conjunto_x = {"JavaScript"} #las llaves sirven para set y dict
print(type(conjunto_vacio))
print(type(conjunto_x))
#inicialisando Set
colores = {"Azul", "Rojo", "Amarillo", "Verde", "Violeta"}
animales = set({"Gato", "Perro", "Caballo", "Hamster"})
print(colores)
print(animales)
#Agregando un nuevo elemento al set
colores.add("Celeste")
print(colores)
