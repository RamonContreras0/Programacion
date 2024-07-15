'''Tres empleados de una fabrica trabajan en dos turnos: diurno y nocturno (10 hrs cada uno). Se busca calcular el pago diario y el total semanal de cada empleado de acuerdo
con los siguientes puntos:
a) La tarifa del turno diurno por hora es de 12000 CLP.
b) La tarifa del turno nocturno por hora es de 16000 CLP.
c) Los domingos la tarifa se incrementa en 2000 CLP el turno diurno y 3000 CLP el turno nocturno.
Ademas considerar:
a) El primer empleado trabaja Lunes, Martes y Miercoles en turnos nocturnos, Jueves y Viernes en turnos diurnos.
b) El segundo empleado trabaja Martes, Miercoles y Jueves turnos nocturnos, y tambien el día domingo en turno diurno.
c) El tercer empleado trabaja Miercoles, Jueves y Viernes diurno, Sabado y Domingo en turnos nocturnos.
Guardar la informacion de cada empleado en un diccionario, con el pago diario que debe recibir cada empleado y el total de la semana.'''

turno_dia = 12000
turno_noche = 16000
turno_dia_domingo = turno_dia + 2000
turno_noche_domingo = turno_noche + 3000
horas_turno = 10


empleados = {
    "Empleado1": {
        "Lunes": "Turno nocturno",
        "Martes": "Turno nocturno",
        "Miercoles": "Turno nocturno",
        "Jueves": "Turno diurno",
        "Viernes": "Turno diurno"
    },
    "Empleado2": {
        "Martes": "Turno nocturno",
        "Miercoles": "Turno nocturno",
        "Jueves": "Turno nocturno",
        "Domingo": "Turno diurno"
    },
    "Empleado3": {
        "Miercoles": "Turno diurno",
        "Jueves": "Turno diurno",
        "Viernes": "Turno diurno",
        "Sabado": "Turno nocturno",
        "Domingo": "Turno nocturno"
    }
}


Empleado1 = (turno_noche * 3 + turno_dia *2)
Empleado2 = (turno_noche * 3 + turno_dia_domingo)
Empleado3 = (turno_dia * 3 + turno_noche_domingo + turno_noche)

print("El sueldo semanal del primer empleado es: ", Empleado1)
print("El sueldo semanal del segundo empleado es: ", Empleado2)
print("El sueldo semanal del tercer empleado es: ", Empleado3)
