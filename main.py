import fun as ff
from os import system as ss

op = 0

empleados = []
ff.generar_sueldos(empleados)

while op !=4:
    ss("cls")
    ff.menu()
    op = ff.validar_op()
    if op==1:
        ss("cls")
        ff.asignar_sueldos(empleados)
        ss("pause")
    elif op==2:
        ss("cls")
        ff.clasificar_sueldos(empleados)
        ss("pause")
    elif op==3:
        ss("cls")
        ff.imprimir_estadisticas(empleados)
        ss("pause")
    elif op==4:
        ss("cls")
        ff.report_sueldos(empleados)
        ss("pause")
    else:
        op==5:
        ss("cls")
print("Finalizando programa")
print("creado por javier menares")