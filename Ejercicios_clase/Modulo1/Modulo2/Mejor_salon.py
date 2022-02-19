estu1={"nombre":"Luis","mat":3.2,"esp":3.0,"ciencias":4.0,"lite":3.5,"arte":5.0}
estu2={"nombre":"marta","mat":4.2,"esp":3.4,"ciencias":4.3,"lite":3.7,"arte":4.8}
estu3={"nombre":"Jose","mat":5.0,"esp":4.2,"ciencias":4.0,"lite":3.8,"arte":4.0}
estu4={"nombre":"Francisco","mat":2.2,"esp":3.0,"ciencias":3.5,"lite":3.2,"arte":3.0}
estu5={"nombre":"Lucas","mat":3.7,"esp":3.5,"ciencias":3.4,"lite":3.3,"arte":5.0}

prom_estu1=round((estu1["mat"]+estu1["esp"]+estu1["ciencias"]+estu1["lite"]+estu1["arte"])/5,2)
prom_estu2=round((estu2["mat"]+estu2["esp"]+estu2["ciencias"]+estu2["lite"]+estu2["arte"])/5,2)
prom_estu3=round((estu3["mat"]+estu3["esp"]+estu3["ciencias"]+estu3["lite"]+estu3["arte"])/5,2)
prom_estu4=round((estu4["mat"]+estu4["esp"]+estu4["ciencias"]+estu4["lite"]+estu4["arte"])/5,2)
prom_estu5=round((estu5["mat"]+estu5["esp"]+estu5["ciencias"]+estu5["lite"]+estu5["arte"])/5,2)


def mejor_salon(estu1,estu2,estu3,estu4,estu5):
    dicc_mejor_est={}
    if prom_estu1 >= prom_estu2 and prom_estu1>=prom_estu3 and prom_estu1>=prom_estu4 :
        dicc_mejor_est[estu1["nombre"]]=prom_estu1
    elif prom_estu2 >= prom_estu1 and prom_estu2>=prom_estu3 and prom_estu2>=prom_estu4 :
         dicc_mejor_est[estu2["nombre"]]=prom_estu2
    elif prom_estu3>=prom_estu1 and prom_estu3>=prom_estu2 and prom_estu3>prom_estu4 :
        dicc_mejor_est[estu3["nombre"]]=prom_estu3
    elif prom_estu4>=prom_estu1 and prom_estu4>=prom_estu2 and prom_estu4>prom_estu3:
        dicc_mejor_est[estu4["nombre"]]=prom_estu4
    return dicc_mejor_est

estudiante_destacado=mejor_salon(estu1,estu2,estu3,estu4,estu5)

print("el mejor estudiante del salón es: ",estudiante_destacado,"dentro del universo de datos que es :")
    

dicc_estu_promedio={}
dicc_estu_promedio[estu1["nombre"]]=prom_estu1
dicc_estu_promedio[estu2["nombre"]]=prom_estu2
dicc_estu_promedio[estu3["nombre"]]=prom_estu3
dicc_estu_promedio[estu4["nombre"]]=prom_estu4
dicc_estu_promedio[estu5["nombre"]]=prom_estu5

print(dicc_estu_promedio)
