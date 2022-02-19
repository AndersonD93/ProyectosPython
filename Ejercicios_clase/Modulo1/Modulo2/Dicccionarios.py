# numero=int(input("ingrese el numero de 10 cifras: "))
# conteo={}
# digito=numero%10
# if digito in conteo :
#     conteo[digito] +=1
# else:
#     conteo[digito]=1
# numero=numero//10
# digito=numero%10
# if digito in conteo :
#     conteo[digito] +=1
# else:
#     conteo[digito]=1
# numero=numero//10
# digito=numero%10
# if digito in conteo :
#     conteo[digito] +=1
# else:
#     conteo[digito]=1
# numero=numero//10
# digito=numero%10
# if digito in conteo :
#     conteo[digito] +=1
# else:
#     conteo[digito]=1
# numero=numero//10
# digito=numero%10
# if digito in conteo :
#     conteo[digito] +=1
# else:
#     conteo[digito]=1
# numero=numero//10
# digito=numero%10
# if digito in conteo :
#     conteo[digito] +=1
# else:
#     conteo[digito]=1
# numero=numero//10
# digito=numero%10
# if digito in conteo :
#     conteo[digito] +=1
# else:
#     conteo[digito]=1
# numero=numero//10
# digito=numero%10
# if digito in conteo :
#     conteo[digito] +=1
# else:
#     conteo[digito]=1
# numero=numero//10
# digito=numero%10
# if digito in conteo :
#     conteo[digito] +=1
# else:
#     conteo[digito]=1
# numero=numero//10
# digito=numero%10
# if digito in conteo :
#     conteo[digito] +=1
# else:
#     conteo[digito]=1
# print(conteo)

# def contar(num:int,dicc:dict)->dict:
#     digito=num%10
#     if digito in dicc:
#         dicc[digito]+=1
#     else:
#         dicc[digito]=1
#     return dicc

# num=int(input("Ingrese numero de 10 digitos"))
# conteo={}
# conteo=contar(num,conteo)
# num=num//10
# conteo=contar(num,conteo)
# num=num//10
# conteo=contar(num,conteo)
# num=num//10
# conteo=contar(num,conteo)
# num=num//10
# conteo=contar(num,conteo)
# num=num//10
# conteo=contar(num,conteo)
# num=num//10
# conteo=contar(num,conteo)
# num=num//10
# conteo=contar(num,conteo)
# num=num//10
# conteo=contar(num,conteo)
# num=num//10
# conteo=contar(num,conteo)
# num=num//10
# print(conteo)

# def contar(num:int,dicc:dict)->int:
#     digito=num%10
#     dicc[digito]=dicc.get(digito,0)+1
#     return num//10

# num=int(input("Ingese numero de 5 cifras :"))
# cont={}
# num=contar(num,cont)
# num=contar(num,cont)
# num=contar(num,cont)
# num=contar(num,cont)
# num=contar(num,cont)

# print(cont)
#_______________________________________________
# def picas_fijas(intento:int,real:int):
#     digito_intento=intento%10
#     digito_real=real%10
    
#     if (digito_intento==digito_real):
#        picasfijas["fijas"]+=1
#     elif str(digito_intento) in str(real2):
#         picasfijas["picas"]+=1
#     return (picasfijas)

# intento=int(input("Ingrese numero de 4 digitos (adivinar) :"))
# real2=int(input("Ingrese numero de 4 digitos (real) :"))
# picasfijas={}
# picasfijas["fijas"]=0
# picasfijas["picas"]=0
# picasfijas=picas_fijas(intento,real2)
# intento=intento//10
# real1=real2//10
# picasfijas=picas_fijas(intento,real1)
# intento=intento//10
# real1=real1//10
# picasfijas=picas_fijas(intento,real1)
# intento=intento//10
# real1=real1//10
# picasfijas=picas_fijas(intento,real1)
# intento=intento//10
# real1=real1//10

# print(picasfijas)
#__________________________
# picasfijas={}
# picasfijas["picas"]=1
# picasfijas["fijas"]=0
# print(picasfijas)

# picas_fijas={}

# picas_fijas["fijas"]=0
# picas_fijas["picas"]=0

# picas_fijas["fijas"]+=1
# picas_fijas["picas"]+=2

# print(picas_fijas)

# print (str(4) in str(4122))

def crear_estudiantes(nom:str,cod:str,gen:str,carr:str,prom:float,ssc:int)->dict:
    dic_estudiante={"nombre":nom,
                    "codigo":cod,
                    "genero":gen,
                    "carrera":carr,
                    "promedio":prom,
                    "ssc":ssc}
    return dic_estudiante

estudiante1=crear_estudiantes("martha","123","F","ING",2.9,1)
estudiante2=crear_estudiantes("Olga","224","F","ING",3.2,2)
estudiante3=crear_estudiantes("Jose","335","M","ING",3.0,3)
estudiante4=crear_estudiantes("Josefa","446","F","ING",4.2,4)


# estudiante1=crear_estudiantes(input("ingrese Nombre :"),input("ingrese codigo :"),input("ingrese sexo :"),input("ingrese carrera :"),float(input("ingrese prom :")))
# estudiante2=crear_estudiantes(input("ingrese Nombre :"),input("ingrese codigo :"),input("ingrese sexo :"),input("ingrese carrera :"),float(input("ingrese prom :")))
# estudiante3=crear_estudiantes(input("ingrese Nombre :"),input("ingrese codigo :"),input("ingrese sexo :"),input("ingrese carrera :"),float(input("ingrese prom :")))
# estudiante4=crear_estudiantes(input("ingrese Nombre :"),input("ingrese codigo :"),input("ingrese sexo :"),input("ingrese carrera :"),float(input("ingrese prom :")))
estudiantes_totales={}
estudiantes_totales[estudiante1["nombre"]]=estudiante1["codigo"]
estudiantes_totales[estudiante2["nombre"]]=estudiante2["codigo"]
estudiantes_totales[estudiante3["nombre"]]=estudiante3["codigo"]
estudiantes_totales[estudiante4["nombre"]]=estudiante4["codigo"]

print("los estudiantes son:",estudiantes_totales)

def mayor_prom(est1:dict,est2:dict,est3:dict,est4:dict):
    mayor=est1
    if(est2["promedio"]>=mayor["promedio"]):
        mayor=est2
    if(est3["promedio"]>=mayor["promedio"]):
        mayor=est3
    if(est4["promedio"]>mayor["promedio"]):
        mayor=est4
    return mayor

mejor=mayor_prom(estudiante1,estudiante2,estudiante3,estudiante4)
print("El estudiante con mejor promedio es :",mejor["nombre"],"con un promedio de:",str(mejor["promedio"]))

def hay_mujer(est1:dict,est2:dict,est3:dict,est4:dict):
    hay_mujer=0
    if (est1["genero"]=="F"):
        hay_mujer+=1
    if(est2["genero"]=="F"):
        hay_mujer+=1
    if(est3["genero"]=="F"):
        hay_mujer+=1
    if(est4["genero"]=="F"):
        hay_mujer+=1
    return hay_mujer
cantidad_mujeres=hay_mujer(estudiante1,estudiante2,estudiante3,estudiante4)
print("la cantidad de mujeres son",cantidad_mujeres)

#Imprime la mujer con mayor promedio del grupo
def mujer_pila(est1:dict,est2:dict,est3:dict,est4:dict):
    mpila={}
    # if (est1["genero"]=="F"):
    #     if (est1["promedio"]>=est2["promedio"])or (est1["promedio"]>=est3["promedio"])or (est1["promedio"]>=est4["promedio"]):
    #         mpila=est1
    # if (est2["genero"]=="F"):
    #     if (est2["promedio"]>=est1["promedio"])or (est2["promedio"]>=est3["promedio"])or (est2["promedio"]>=est4["promedio"]):
    #         mpila=est2
    # if (est3["genero"]=="F"): 
    #     if (est3["promedio"]>=est1["promedio"])or (est3["promedio"]>=est2["promedio"])or (est3["promedio"]>=est4["promedio"]):
    #         mpila=est3
    # if (est4["genero"]=="F"): 
    #     if (est4["promedio"]>=est1["promedio"])or (est4["promedio"]>=est2["promedio"])or (est4["promedio"]>=est3["promedio"]):
    #         mpila=est4
    # else:
    #     print("No hay mujeres en el grupo")
    # return mpila
    if (est1["genero"]=="F"):
        mpila[est1["nombre"]]=[est1["promedio"]]
    if (est2["genero"]=="F"):
        mpila[est2["nombre"]]=[est2["promedio"]]
    if (est3["genero"]=="F"):
        mpila[est3["nombre"]]=[est3["promedio"]]
    if (est4["genero"]=="F"):
        mpila[est4["nombre"]]=[est4["promedio"]]
    return mpila
    
Mujeres_nombre=mujer_pila(estudiante1,estudiante2,estudiante3,estudiante4)
print("Las mujeres del grupo son :",Mujeres_nombre)

#dicc= {"nombre":"jesus","sexo":"f"}
#dicc2={"maria":"m","sexo":"f"}
# # conteo=0
# # if (dicc["sexo"]=="f"):
# #     conteo+=1
# # if (dicc2["sexo"]=="f"):
# #     conteo+=1
# # print(conteo)

#print(dicc,dicc2)

def buscar_est(estudiante1,estudiante2,estudiante3,estudiante4,nombre:str):
    est_encontrado= None
    if estudiante1["nombre"] == nombre:
        est_encontrado=estudiante1
    elif estudiante2["nombre"] == nombre:
        est_encontrado=estudiante2
    elif estudiante3["nombre"] == nombre:
        est_encontrado=estudiante3
    elif estudiante4["nombre"] == nombre:
        est_encontrado=estudiante4
    return est_encontrado

estudiante_encontrado=buscar_est(estudiante1,estudiante2,estudiante3,estudiante4,"Juan")

if estudiante_encontrado is None :
    print("El estudiante no existe")
else:    
    print("El estudiante existe y su codigo es",estudiante_encontrado["codigo"])

def nuevo_semestre(est1,est2,est3,est4)->None:
    est1["ssc"]+=1
    est2["ssc"]+=1
    est3["ssc"]+=1
    est4["ssc"]+=1

print (estudiante1)
nuevo_semestre(estudiante1,estudiante2,estudiante3,estudiante4)
print(estudiante1)

def est_riesgo (e_1,e_2,e_3,e_4)->dict:
    est_en_riego={}

    if e_1["promedio"]<3.4:
        est_en_riego[e_1["nombre"]]=e_1["promedio"]
    
    if e_2["promedio"]<3.4:
        est_en_riego[e_2["nombre"]]=e_2["promedio"]
        
    if e_3["promedio"]<3.4:
        est_en_riego[e_3["nombre"]]=e_3["promedio"]
        
    if e_4["promedio"]<3.4:
        est_en_riego[e_4["nombre"]]=e_4["promedio"]
       
    return est_en_riego

Estudiantes_en_riesgo=(est_riesgo(estudiante1,estudiante2,estudiante3,estudiante4))
print("Los estudiantes en riesgo son:",Estudiantes_en_riesgo)

