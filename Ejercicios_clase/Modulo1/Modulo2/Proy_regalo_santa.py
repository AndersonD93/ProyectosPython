# print(242%10)
# print(round(242/100))
# print(241%2==0)

def clasificar_regalo (codigo:int):
    clasificacion=()
    if round(codigo%10)==round(codigo/100) and (codigo%2!=0): 
        clasificacion="Corresponde a niña"
    elif round(codigo%10)==round(codigo/100) and (codigo%2==0):
        clasificacion="Corresponde a niño"
    elif round(codigo%10)!=round(codigo/100) and (codigo%2==0):
        clasificacion="Correponde a hombre"
    else:
        clasificacion="Corresponde a mujer"
    return clasificacion

#PROGRAMA PRINCIPAL
codigo= (int(input("Codigo de regalo entre 100 y 999 :")))
clasificacion_final=clasificar_regalo(codigo)

print ("El regalo con codigo ", codigo," ",clasificacion_final)
