def calcular_imc (peso:float, altura:float)-> float:
    return peso/(altura)**2

def calcular_porcentaje_grasa (peso:float,altura:float,edad:float,valorg:float)-> float:
    return (1.2* ((peso/(altura)**2)+0.23)*edad)-5.4-valorg

def tasa_metabolica_basal (peso:float,altura:float,edad:float,valorg:float)-> float:
    return (10*peso)+(6.25*altura)-(5*edad)+valorg

def TMB_af (peso:float,altura:float,edad:float,valorg:float,valoract:float)-> float:
    return ((10*peso)+(6.25*altura)-(5*edad)+valorg)*valoract

    
   
