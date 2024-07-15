'''
Se cuenta con dos sets: el primero contiene las temperaturas mínimas tomadas el mes de Mayo en Castro.
El segundo set contiene las temperaturas máximas del mes de Mayo en Castro. (60 Puntos)
● Temperaturas Mínimas = {9, 5, 2, 7, 6, 1}
● Temperaturas Máximas = {12, 14, 11, 10, 15, 9}
A) Verificar si la temperatura 9°C se encuentra en ambos sets utilizando condicionales.
B) Unir ambos sets en un solo y eliminar duplicados. Imprimir el set generado.
C) Transformar el set en una lista, y encontrar las temperatura mínima y máxima utilizando bucles. Imprimir los resultados.
D) Crear una tupla con los valores de temperaturas mínima y máxima, más un string
con las etiquetas de texto: “Mínima” y “Máxima”. Imprimir la tupla generada.
E) Generar e imprimir un diccionario donde las claves sean las temperaturas y los
valores sean la frecuencia de aparición.
'''

Temperaturas_Mínimas = {9, 5, 2, 7, 6, 1}
Temperaturas_Máximas = {12, 14, 11, 10, 15, 9}

#A)
if 9 in Temperaturas_Máximas and 9 in Temperaturas_Mínimas:
    print(" La temperatura 9 se encuetra en ambos set")
else:
    print("La temperatura 9 no se encuentra en ambos set")

#B) 
Temperaturas_Mínimas= list(Temperaturas_Mínimas)
Temperaturas_Máximas= list(Temperaturas_Máximas)

Temperaturas = Temperaturas_Máximas + Temperaturas_Mínimas
Temperaturas = set(Temperaturas)
print(Temperaturas)

#C)
Temperaturas= list(Temperaturas)
Minima= min(Temperaturas)
Maxima= max(Temperaturas)
print(f"La temperatura minima es: {Minima} y la maxima es: {Maxima}")

#D) 
Maxima= tuple(Maxima)
Minima= tuple(Minima)

#E)
Temperaturas =(
    "1 : 1"
    "2 : 1"
    "5 : 1"
    "6 : 1"
    "7 : 1"
    "9 : 1"
    "10 : 1"
    "11 : 1"
    "12 : 1"
    "14 : 1"
    "15 : 1"
)