# sumatoria=0
# i=1
# iteraciones=0
# while i<=10000:
#     iteraciones+=1
#     sumatoria +=i
#     i +=1 
# print("El resultado de la sumatoria es :",sumatoria)
# print("El No de iteraciones es:",iteraciones)
# print("El valor de i es :",i)

# from math import sqrt

# x=float(input("Favor ingrese un No positivo: "))

# while x<0:
#     print("Solo puede ingresar valores positivos")
#     x=float(input("Favor ingrese un No positivo: "))
# print ("La raiz cuadrada de ",x," es ",sqrt(x))
# print("El resultado es : {0} de la raiz cuadrada de: {1}".format(sqrt(x),x))

# n1=(int(input("ingrese su primer No: ")))
# n2=(int(input("ingrese su segundo No: ")))

# def maximo_comun_divisor(n1,n2):
#     n=min(n1,n2)
#     encontro= False
#     while (encontro== False):
#         if (n1%n==0 and n2%n==0):
#             encontro= True
#         else:
#             n= n-1
#     return n
# print ("el maximo común divisor entre {a} y {b} es".format(a=n1,b=n2),maximo_comun_divisor(n1,n2))

# digito=input("Ingrese su numero :")
# def contador_de_digitos(digito):
#     return len(digito)
# print("La cantidad de digitos en:{a} es :".format(a=digito),contador_de_digitos(digito))

# def factorial(n):
#     terminar= False
#     factorial=1
#     while (terminar== False):
#        if n==0:
#            terminar=True
#        else:
#             factorial *=n 
#             n -=1
#     return  factorial
# n=int(input("ingrese numero : "))
# while n<0:
#     print("No se permiten Numeros negativos:")
#     n=int(input("ingrese numero : "))
# print("El resultado del factorial para {a} es".format(a=n),factorial(n))

# def sucesion_fibonacci(sucesion):
#     terminar= False
#     cantidad_sucesiones=0
#     n1=0
#     n2=1

#     while (terminar==False):
#         if cantidad_sucesiones == sucesion:
#             terminar= True
#         elif cantidad_sucesiones += 1
            
#     return cantidad_sucesiones
# sucesion= int(input("ingrese el numero de sucesiones :"))
# print (sucesion_fibonacci(sucesion))

# termino=False
# cant=0
# sumatoria=0
# n1=0
# n2=2


# while (termino==False):
#     if cant>=15:
#         termino=True
#     elif n3=n1+n2
# print(sumatoria)

def sucesion_fibonacci(n):
    a = 0 
    b = 1
    repeticion=0
    termino= False
    while (termino== False):
        if repeticion < n:
            print(a)
            repeticion +=1
            (a,b) = (b,a+b)
        else:
            termino= True
    return " "

n=int(input("Ingrese el No de sucesiones :"))
print (sucesion_fibonacci(n))