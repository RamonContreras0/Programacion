"""Crear un algoritmo que permita ingresar y gestionar las notas de un estudiante en tres asignaturas diferentes,
utilizando diccionarios, tuplas, sets y listas. El algoritmo debe calcular el promedio final ponderado de cada
estudiante por asignatura y mostrar toda la información ingresada."""

Nombre = "Ramon"
asignatura1 = "Matematicas"
nota1 = 5.8
nota2 = 6.2
nota3 = 5.4
asignatura2 = "Programacion"
nota4 = 4.8
nota5 = 5.2
nota6 = 6.2
asignatura3 = "Taller"
nota7 = 7.0
nota8 = 6.2
nota9 = 3.2

promedio1 = ((nota1 * 0.3) + (nota2 * 0.5) + (nota5 * 0.2))
promedio1= round(promedio1,1)
print(f"EL promedio es de:  {promedio1:.1f}")
notas1=set({nota1, nota2,nota3})
promedio2 = ((nota4 * 0.3) + (nota5 * 0.5) + (nota6 * 0.2))
promedio2= round(promedio2,1)
print(f"EL promedio es de:  {promedio2:.1f}")
notas2=set({nota4,nota5,nota6})
promedio3 = ((nota7 * 0.3) + (nota8 * 0.5) + (nota9 * 0.2))
promedio3= round(promedio3,1)
print(f"EL promedio es de:  {promedio3:.1f}")
notas3=set({nota7,nota8,nota9})
promediof = (promedio1 + promedio2 + promedio3)/3
promediof = round(promediof,1)
print(f"EL promedio final es de:  {promediof:.1f}")
Asignaturas = ("Matematicas", "Programacion", "Taller")
Ramon = {
    "Asignaturas" : Asignaturas,
    "Notas Matematicas" : notas1,
    "Promedio Matematicas" : promedio1,
    "Notas Programacion" : notas2,
    "Promedio Programacion" : promedio2,
    "Notas Taller" : notas3,
    "Promedio Taller" : promedio3,
    "Promedio total" : promediof
    }
print(Ramon)
