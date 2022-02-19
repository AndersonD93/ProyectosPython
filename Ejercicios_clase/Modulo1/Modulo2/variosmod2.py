# a=45
# b=30
# c=10

# print(a>b and c)

#condicionales
# import math

# x= int(input("Digite el numero"))
# if x<0 :
#     print ("Ese Hp numero no aplica acá dado que ", x, "es negativo")
#     y=x
#     x=42
#     print("en vez de ese malp numero decidi utilizar ",x)

# print ("la raiz cuadrada de ",x,"es",math.sqrt(x))


# num1=(int(input("Digite su primer Numero: ")))
# num2=(int(input("Digite su 2do Numero: ")))
# num3=(int(input("Digite su 3er Numero: ")))

# cantidad_pares=0
# if num1%2==0:
#     cantidad_pares +=1
# if num2%2==0:
#     cantidad_pares +=1
# if num3%2==0:
#     cantidad_pares +=1
# print("la cantidad de No pares son",cantidad_pares)

# def numero_mayor (n1:int,n2:int,n3:int,n4:int):
#  n1=(int(input("Digite su primer Numero: ")))
#  n2=(int(input("Digite su 2do Numero: ")))
#  n3=(int(input("Digite su 3er Numero: ")))
#  n4=(int(input("Digite su 4to Numero: ")))
#  if (n1>=n2) and(n1>=n3) and (n1>=n4):
#     nm=n1
#  elif (n2>=n1) and(n2>=n3) and (n2>=n4):
#     nm=n2
#  elif (n3>=n1) and(n3>=n2) and (n3>=n4):
#     nm=n3
#  else:nm=n4
#  return nm
 
# print (numero_mayor(1,2,3,4))

# def num_mayor_simple(a,b,c,d):
#     a=(int(input("Digite su primer Numero: ")))
#     b=(int(input("Digite su 2do Numero: ")))
#     c=(int(input("Digite su 3er Numero: ")))
#     d=(int(input("Digite su 4to Numero: ")))
#     mayor= a
#     if (b>mayor):
#         mayor=b
#     if (c>mayor):
#         mayor=c
#     if (d>mayor):
#         mayor=d
#     return mayor
# print(num_mayor_simple(1,2,3,4))

# def edad_pase (edad:int):
#     return(edad>=16)
# print (edad_pase(int(input("Ingrese su edad: "))))

# def definir_numero(num:int):
#     num=(int(input("Ingrese su numero :")))
#     valor= 0
#     if num<0:
#         valor=-1
#     if num>0 and num<1000:
#         valor=0
#     if num>1000 and num<=10000:
#         valor=1
#     if num>=10000:
#         valor=2
#     return valor
# print (definir_numero(1))

# def divisible(n,d):
#     n=(int(input("ingrese su primer numero :")))
#     d=(int(input("ingrese su segundo numero :")))
#     if (n%(2*d))==0 or (n%d)==0 :
#         valor= "si es divisible"
#     else:
#         valor="no es divisible"
#     return valor
#print(divisible(2,10))
# def puntos_alineados (x1,x2,x3,y1,y2,y3):
#     if ((y2-y1)/(x2-x1)) == ((y3-y2)/(x3-x2)): 
#         alineado= "True"
#     else: 
#         alineado= "false"
#     return alineado
# print(puntos_alineados(-5,-1,1,3,-3,-6))

def precio_tiquete (cia:str,edad:int,temp:bool,est:bool):
    
    precio=5000000
    if cia=="VOLAR" and temp :
        preciof= precio *(1+0.2)
    elif  cia=="ALAS" and temp :
        preciof=precio*(1+0.3)
    else: preciof=precio
    valor_segun_edad=0
    if edad< 16:
        valor_segun_edad=preciof/-2
    if edad> 60:
        valor_segun_edad=100000
    descuento_estudiantil=0
    if cia=="ALAS" and edad>16 and temp==False  and est:
        descuento_estudiantil= preciof*0.1
    return round(preciof+valor_segun_edad-descuento_estudiantil)
#PROGRAMA PRINCIPAL
cia=(input("Ingrese con que compañia desea volar (VOLAR/ALAS) :"))
edad=(int(input("Ingrese su edad :")))
temp=(bool(input("Es temporada alta? escriba 1 para si y 0 para no :")))
est= (bool(input("Es estudiante ? escriba 1 para si y 0 para no:")))

tarifa_final=precio_tiquete(cia,edad,temp,est)

print ("El valor final de su tiquiete es : $",tarifa_final)