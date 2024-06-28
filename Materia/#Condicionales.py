#Condicionales
edad = int(input("Ingrese la edad de la persona"))

if edad < 0 or edad >= 120: 
    categoria = "Edad no Valida"
elif edad <= 12:
    categora = "Niño/a"
elif edad <= 17:
    categoria = "Adolecente"
elif edad <= 64:
    categoria = "Adulto"
else:
    categoria = "Adulto Mayor"

print(f"La persona es: {categoria}")