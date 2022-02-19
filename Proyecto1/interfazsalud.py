# from Logica.logicasalud import *
import Logica.logicasalud as logic


peso=(float(input("Ingrese su Hp peso: ")))
altura= (float(input("Ingrese su Hp Altura :")))
edad= float(input("Ingrese su malp edad :"))
valorg=0
genero = (str(input("ingrese su sexo: ")))
if (genero=="H"):
 valorg= 10.8
else: valorg=0


def ejecalcular_imc(pe:float,al:float)->None:
   IMC= logic.calcular_imc(peso,altura)

def ejecalcular_porcentaje_grasa(p,h,e,v):
   dato = logic.calcular_porcentaje_grasa(p,h,e,v)
   return dato

print(ejecalcular_porcentaje_grasa(p=peso,h=altura,v=valorg,e=edad))
