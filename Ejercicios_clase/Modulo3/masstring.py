# fruta="manzana"
# cadena1=fruta[::1]
# cadena2=fruta[::2]
# cadena3=fruta[::-1]
# print(cadena1)
# print(cadena2)
# print(cadena3)

# def ocurrencias_numero(palabra:str,letra:str):#cuenta la cantidad de ocurrencias de la letra en la palabra
#     ocurrencia=0
#     digito_palabra=0
#     while (digito_palabra< len(palabra)):
#         if (palabra[digito_palabra]==letra):
#             ocurrencia+=1
            
#         digito_palabra+=1
    
#     return ocurrencia
# # print("El numero de ocurrencias es:",ocurrencias_numero("Lucas","L"))
# # print("El numero de ocurrencias es:",ocurrencias_numero("Lucasiño","a"))
# print("El numero de ocurrencias es:",ocurrencias_numero("Marilucas","a"))

def palindrome(palabra:str):
    termino=False
    sin_espacios=palabra.replace(" ","")
    en_minus=sin_espacios.lower()
    while termino==False :
        if en_minus==en_minus[::-1]:
            termino=True
        else:
            termino="False"
    
    return termino

print (palindrome("Isaac no ronca asi"))
print (palindrome("Sometamos o Matemos"))
print (palindrome("vencer o Morir"))
print (palindrome("Ama"))


