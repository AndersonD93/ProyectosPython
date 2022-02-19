import logicadivisas as logdiv

    
def ejecutar_convertir_a_dolares(trm:float)->None:
    pesos = float(input("ingrese la cantidad de cop: "))
    dolares = logdiv.convertiradolares(pesos, trm)
    print(pesos,"pesos son,",round(dolares,2),"dolares")
    
def ejecutar_convertir_a_pesos(trm:float)->None:
    dolares = float(input("ingrese la cantidad de usd: "))
    pesos = logdiv. convertirapesos(dolares, trm) 
    print(dolares,"dolares son,",round(pesos),"pesos") 

    
def iniciar_aplicacion ():
    trm = float(input("ingrese valor de TRM: "))
    ejecutar_convertir_a_dolares(trm)
    ejecutar_convertir_a_pesos(trm)
     

iniciar_aplicacion()