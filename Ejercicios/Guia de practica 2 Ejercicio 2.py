'''2. Desarrollar un algoritmo que solicite al usuario una cadena de texto y cuente cuántas veces
aparecen las vocales 'a', 'e', 'i', 'o' y 'u' en la cadena de texto. Utilizar ciclos para resolver el
problema.# Solicitar al usuario una cadena de texto'''


cadena = input("Ingrese una cadena de texto: ")
cadena = cadena.lower()

a = 0
e = 0
i = 0
o = 0
u = 0

# Recorrer la cadena de texto y contar las vocales
for caracter in cadena:
    if caracter == 'a':
        a += 1
    elif caracter == 'e':
        e += 1
    elif caracter == 'i':
        i += 1
    elif caracter == 'o':
        o += 1
    elif caracter == 'u':
        u += 1

# Mostrar el conteo de cada vocal
print(f"La vocal 'a' aparece {a} veces.")
print(f"La vocal 'e' aparece {e} veces.")
print(f"La vocal 'i' aparece {i} veces.")
print(f"La vocal 'o' aparece {o} veces.")
print(f"La vocal 'u' aparece {u} veces.")
