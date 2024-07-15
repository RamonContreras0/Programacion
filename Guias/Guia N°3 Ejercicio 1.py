''' Obtener la cantidad de veces que se repite la palabra “universidad” dentro del siguiente
parrafo: 
“La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional 
entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus 
pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participación
democratica.” 
Guardar las palabras encontradas dentro de una tupla.'''

parrafo= """La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional 
entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus 
pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participación
democratica."""

Universidad=parrafo.count("Universidad") + parrafo.count("universidad")
print(Universidad)

palabras= tuple(parrafo.split())
print(palabras)
print ("La palabra Universidad aparece", Universidad, "veces ")
