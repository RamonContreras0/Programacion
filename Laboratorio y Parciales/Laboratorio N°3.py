ID_14 = {
    "Región": "Los Ríos",
    "Superficie (Km2)": 18429,
    "Habitantes": 404432
}

ID_12 = {
    "Región": "Magallanes",
    "Superficie (Km2)": 1382291,
    "Habitantes": 166533
}

censo_2017 = {
    "ID_14": ID_14,
    "ID_12": ID_12
}

print(censo_2017)

densidad1 = ID_14["Superficie (Km2)"] / ID_14["Habitantes"]
densidad1 = round(densidad1, 1)  
densidad2 = ID_12["Superficie (Km2)"] / ID_12["Habitantes"]
densidad2 = round(densidad2, 1)  

ID_14.update({"Densidad": densidad1})
ID_12.update({"Densidad": densidad2})

ID_14.update({"Capital": "Valdivia"})
ID_12.update({"Capital": "Punta Arenas"})

ID_14.update({"Comunas": "Río Bueno, La Unión, Paillaco"})
ID_12.update({"Comunas": "Cabo de Hornos, Puerto Williams, Porvenir"})

ID_14.update({"Provincias": "Ranco, Valdivia "})
ID_12.update({"Provincias": "Antártica Chilena, Magallanes, Tierra del Fuego, Última Esperanza"})

ID_12.update({"Región": "Magallanes y Antártica Chilena"})

print(censo_2017)

lista = list(censo_2017.items())
print(lista)