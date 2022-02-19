#def cuadrado(x:float):
#    return x**2
#print(cuadrado(2))
#a=1+cuadrado(3)
#print(cuadrado(a*3))


#def area_rectangulo(altura:float, anchura:float):
#    return altura * anchura

#x= float(input("indique el valor de la altura del triangulo"))
#y= float(input("indique el valor de la anchura del triangulo"))
#a = area_rectangulo (x,y)
#print("el area de su triangulo es",a)

#def value_intr():
#    return int(input("digite No."))

#valor= value_intr()
#print("el valor tecleado es:",valor)

#def area_triangulo(s1:float,s2:float,s3:float):
#    return (s1+s2+s3)/2

#s1=float(input("valor l1 :"))
#s2=float(input("valor l2 :"))
#s3=float(input("valor l3 :"))

#s=area_triangulo(s1, s2, s3)
#import math
#print("el area del triangulo es",str(round(math.sqrt(s))))

#def indice_bmi (alt:float,peso:float):
#    return peso / (alt**2)

#alt= float(input("ingrese su altura en pulgadas :"))*0.025
#peso= float(input("ingrese su peso en libras :"))*0.45

#print("su altura es : ",round(alt,2), "y su peso es",round(peso,2), "su bmi es:",round(indice_bmi(alt, peso),2))

#def Consumo_GasolinaCOP(precio_galon:float,km_recorridos:float, galones_consumidos:float):
#  return (km_recorridos/galones_consumidos)*precio_galon

#km_recorridos= (float(input("indique los km recorridos en el ultimo mes :")))
#precio_galon= (float(input("indique el valor del galon en cop :")))
#galones_consumidos= (float(input("indique cuantos km por lt rinde su automovil :"))/0.2641)

#print("para un consumo de ",round(galones_consumidos,2),"Km/galon, el gasto del combustible es $",round(Consumo_GasolinaCOP(precio_galon, km_recorridos, galones_consumidos)))

#def farenhait_centigrados (fare: float):
#    return (fare-32)*5/9
#fare=(float(input("indique los grados farenheit")))
#print("los grados centigrados son:",round(farenhait_centigrados(fare),2))

#def centigrados_farenhait(centi:float):
#    G_faren= (centi*(9/5))+32
#    return G_faren

#def radianes_a_grados(radian:float):
#    pi = 3.1416
#    return (radian*360)/(2*pi) 
#def invertir_numeros(numero:int):
#    unidades=numero % 10
 #   numero //=10
#    decenas=numero % 10
#    numero //=10
#    centenas= numero%10
#    numero //=10
#    miles=numero%10
#    numero //=10
    
#    invertir=(decenas*100)+(unidades*1000)+(centenas*10)+(miles*1)
    
#    return invertir

#print(invertir_numeros(5432))

def cambio_moneda(pesos:int):
    
    a=pesos//500
    pesos%=500
    b=(pesos%500)//200
    pesos%=200
    c=(pesos%200)//100
    pesos%=100
    d=(pesos%100)//50
    
    return "a: "+str(a)+" b:"+str(b)+" c:"+str(c)+" d:"+str(d) 
print(cambio_moneda(8200))    

# def calcular_hora_llegada(hora_salida:int , tiempo_duracion:int):
    
#     hora_salida = (input("ingrese la hora de salida del vuelo en formato HH/MM/SS :"))
#     tiempo_duracion=(input("ingrese el tiempo de duración del vuelo en formato HH/MM/SS :"))
#     minuto_reloj_salida = int((hora_salida.split("/")[1]))
#     segundo_salida=int((hora_salida.split("/")[2]))
#     hora_duracion=int((tiempo_duracion.split("/")[0]))
#     minuto_duracion=int((tiempo_duracion.split("/")[1]))
#     segundo_duracion=int((tiempo_duracion.split("/")[2]))
#     hora_reloj_salida= int((hora_salida.split("/"))[0])

#     return(str(hora_reloj_salida + hora_duracion)+"/"+ str(minuto_reloj_salida + minuto_duracion)+"/"+str(segundo_salida+segundo_duracion))

#     print("su hora exacta de llegada es",calcular_hora_llegada(hora_salida , tiempo_duracion))