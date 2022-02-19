# estudiantes={}
# estudiante1={'nombre': 'Juan', 'codigo': '1', 'genero': 'M', 'carrera': 'ING', 'promedio': 4.9}  
# estudiante2={'nombre': 'maria', 'codigo': '2', 'genero': 'F', 'carrera': 'ING', 'promedio': 4.5}
# estudiante3={'nombre': 'Jose', 'codigo': '3', 'genero': 'M', 'carrera': 'ING', 'promedio': 4.0}
# estudiante4={'nombre': 'Josefa', 'codigo': '4', 'genero': 'F', 'carrera': 'ING', 'promedio': 4.2}


# print("Juan" in estudiante1.values())


def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    dic_peliculas={
                "nombre":nombre,
                "genero":genero,
                "duracion": duracion,
                "anio":anio,
                "clasificacion":clasificacion,
                "hora":hora,
                "dia":dia}                             
    return dic_peliculas
peliculas_creadas1=crear_pelicula("Matriz","ciencia ficcion",120,1994,"a+",34,"viernes")
peliculas_creadas2=crear_pelicula("Avatar","ciencia ficcion",130,2001,"b+",44,"sabado")
print("las peliculas creadas son Pelicula No.1: ",peliculas_creadas1["nombre"],"Pelicula No 2:",peliculas_creadas2["nombre"])
print(type(peliculas_creadas2))

def encontrar_pelicula(nombre_pelicula: str, p1: dict=peliculas_creadas1, p2: dict=peliculas_creadas2) -> dict:
    dicc_peli_encontrada={}
    if nombre_pelicula in p1.values():
        dicc_peli_encontrada=p1
    elif nombre_pelicula in p2.values():
        dicc_peli_encontrada=p2
    else:
        dicc_peli_encontrada="Pelicula no Encontrada"
    return dicc_peli_encontrada

pelicula_encontrada=encontrar_pelicula("King Kong",peliculas_creadas1,peliculas_creadas2)
print("los datos de la pelicula buscada son:",pelicula_encontrada)

def encontrar_pelicula_mas_larga(p1: dict, p2: dict):
    dicc_peli_mas_larga={}
    if peliculas_creadas1["duracion"]>peliculas_creadas2["duracion"]:
        dicc_peli_mas_larga=peliculas_creadas1
    else:
        dicc_peli_mas_larga=peliculas_creadas2
    return dicc_peli_mas_larga

Pelicula_mas_larga=encontrar_pelicula_mas_larga(peliculas_creadas1,peliculas_creadas2)
print("La pelicula mas larga es :",Pelicula_mas_larga["nombre"],"con un tiempo de ",Pelicula_mas_larga["duracion"]," minutos")
