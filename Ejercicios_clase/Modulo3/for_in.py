# #sumatoria utilizando for in

# def sumatoria(iteraciones:int):
#     resultado=0
#     for cada_valor in range(1,iteraciones+1):
#         resultado += cada_valor
#     return resultado
# print (sumatoria(1000))

# #sumatoria utilizando while.

# def sumatoriawhile(iteraciones:int):
#     i=1
#     resultado=0

#     while i<= iteraciones:
#         resultado +=i
#         i+= 1
    
#     return resultado

# print (sumatoriawhile(1000))

#Identificar si el numero es primo (mayor a uno solo divisible por 1 y el mismo)

# def num_primo (numero:int):
#     primo= True
#     for valor in range (2,numero):
#         if (numero%valor)==0:
#             primo= False
#     return primo
# print(num_primo(41))


#CUENTA CANTIDAD DE CARACTERES DIFERENTES QUE APARECEN EN LA CADENA
def contar_caracteres_repetidos(cadena:str):
    contar_rep=0
    posicion_caracter=1
    for caracter in cadena:
        if caracter not in cadena[posicion_caracter:]:
            contar_rep +=1
        posicion_caracter +=1
    return contar_rep
print (contar_caracteres_repetidos("AAAS"))

print(sorted("cantara"))





