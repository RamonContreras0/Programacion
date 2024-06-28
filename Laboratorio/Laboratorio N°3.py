
ID_14=dict[
    "Región: " "Los Rios",
    "Superficie(Km2): " "18.429",
    "Habitantes: " "404.432"
]
ID_12=dict [
    "Región: " " Magallanes",
     "Superficie(Km2): " "1.382.291 ",
     "Habitantes: " "166.533"]     

censo_2017=dict[
    ID_14,
    ID_12   
]
print(censo_2017)

densidad1= 18429/404432
densidad1= round(1)
densidad2= 1382291/166533
densidad2= round(1)
"Capital: " "Valdivia"
"Capital: " "Punta Arenas"
"Comunas: " "Río Bueno, La Unión, Paillaco"
"Comunas: " "Cabo de Hornos, Puerto Williams, Porvenir"
"Provincias: " "Ranco, Valdivia"
"Provincias: " "Antártica Chilena, Magallanes, Tierra del Fuego, Última Esperanza"
#ID_12.__add__("Densidad: ", densidad1)
#ID_14.__add__("Densidad: ", densidad2)
ID_14=dict[
    "Región: " "Los Rios",
    "Superficie(Km2): " "18.429",
    "Habitantes: " "404.432",
    "Capital: " "Valdivia",
    "Comunas: " "Río Bueno, La Unión, Paillaco",
    "Provincias: " "Ranco, Valdivia"
    "Densidad: ", densidad1,]
ID_12=dict [
    "Región: " " Magallanes",
     "Superficie(Km2): " "1.382.291 ",
     "Habitantes: " "166.533",
     "Capital: " "Punta Arenas",
     "Comunas: " "Cabo de Hornos, Puerto Williams, Porvenir",
     "Provincias: " "Antártica Chilena, Magallanes, Tierra del Fuego, Última Esperanza"
     "Densidad: ", densidad2]  
#ID_12.update=("Magallanes y Antártica Chilena")
censo_2017=dict[
    ID_14,
    ID_12   
]
print(censo_2017)

list(censo_2017)
