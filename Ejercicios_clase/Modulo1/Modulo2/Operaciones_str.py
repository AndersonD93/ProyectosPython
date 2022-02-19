# b="aa\tbb\n"
# print(b,"\n")
# a="una\ncadena"
# print(a,"\n")
# print("aa\tbb\nxx\tyy\tzz\n")
# print("una cadena\nque ocupa\nmuchas\tlineas")
# b=str.lower("Cruce")
# print (b)
# def funcion (cad1: str, cad2: str)-> int:
#     if cad1 == cad2:
#         resp = 1
#     elif cad1.lower() == str.lower(cad2):
#         resp = 2
#     else:
#         resp = 0
#     return resp
# bb=funcion("cad1","Cad1")
# print(str.lower("Cad1"))
# print("cad1".lower())

# carta= """  
# querido {0}{2}.
# {0}tengo una propuesta para ud """
# print(carta.format("Julio","Mario","Sarmiento"))

# def contar_a(cad1:str,cad2:str,cad3:str,cad4:str):
#     mayor_cadena=cad1
#     a=cad1.lower().count("a")
#     b=cad2.lower().count("a")
#     c=cad3.lower().count("a")
#     d=cad4.lower().count("a")
#     if a>=b and a>=c and a>=d:
#         mayor_cadena=cad1
#     elif b>=a and b>=c and b>=d:
#         mayor_cadena=cad2
#     elif c>=a and c>=b and c>=d:
#         mayor_cadena=cad3
#     else:
#         mayor_cadena=cad4
#     return mayor_cadena

# print(contar_a("Aeropuertaa","AreaticaA","ahora","aliciaa"))

def contar_materias(materia1:str,materia2:str,materia3:str,materia4:str):
    materias=("programacion","matematica","filosofia","literatura")
    conteo_final=0
    if materia1 in materias:
        conteo_final+=1
    if materia2 in materias:
        conteo_final+=1
    if materia3 in materias:
        conteo_final+=1
    if materia4 in materias:
        conteo_final+=1
    return conteo_final

numero_final_materias= contar_materias("ed fisica","religion","filosofia","literatura")
print ("el total de las materias de su gusto son",numero_final_materias)

        
