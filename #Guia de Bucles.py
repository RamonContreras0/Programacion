#Guia de Bucles

#Llamando paquete colorama
from colorama import init, Fore

num = 0 
print(Fore.RED + "Inicio Ciclo N°1")
while num <= 100:
    print(num)
    num = num + 2
    #num += 2
print(Fore.RED + "Cierre de Ciclo N°1")

print(Fore.YELLOW + "Inicio Ciclo N°2" )
while num <= 200:
    print(num)
    num = num +2
else:
    print(Fore.GREEN + "Mi condicion es igual o mayor a 200")
print(Fore.GREEN + "Cierre de Ciclo N°2")

print(Fore.MAGENTA + "Inicio Ciclo N°3")
while num <= 300:
    print(num)
    num = num + 2
    if num == 250:
        print(Fore.MAGENTA + "Se detiene la ejecucion")
        break
print(Fore.CYAN + "Cierre de Ciclo N°3")

#Ciclo For
newlista = [1,2,3,4,5,6,7,8,9,10]

print(Fore.LIGHTGREEN_EX + "Inicio Ciclo N°4 (For)")
for i in newlista:
    print(i)