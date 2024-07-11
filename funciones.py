import csv
import random
import statistics

def asignar_sueldos_aleatorios(trabajadores):
    sueldos_trabajadores = {}

    for trabajador in trabajadores:
        sueldo = random.randint(300000, 2500000)
        sueldos_trabajadores[trabajador] = sueldo

    return sueldos_trabajadores



def clasificar_sueldos(sueldos_trabajadores):
    menores_800={}
    entre_800_2000={}
    mayores_2000={}
    acum_sueldos=0

    for trabajador, sueldo in sueldos_trabajadores.items():
        acum_sueldos = acum_sueldos + sueldo
        if sueldo <800000:
            menores_800[trabajador] = sueldo
        elif sueldo <=2000000:
            entre_800_2000[trabajador] = sueldo
        else:
            mayores_2000[trabajador] = sueldo
    print("")
    print("Nombre empleado","sueldo")
    for trabajador, sueldo in menores_800.items():
        print(trabajador,sueldo)
        
    print("Sueldos menores a $800.000 TOTAL: ", len(menores_800))
    print("")

    print("Nombre empleado","sueldo")
    for trabajador, sueldo in entre_800_2000.items():
        print(trabajador,sueldo)

    print("")   
    print("Sueldos entre $800.000 y $2.000.000 TOTAL: ", len(entre_800_2000))
    print("")

    print("Nombre empleado","sueldo")
    for trabajador, sueldo in mayores_2000.items():
        print(trabajador,sueldo)
        
    print("Sueldos entre $800.000 y $2.000.000 TOTAL: ", len(mayores_2000), '\n')
    
    print("TOTAL SUELDOS: $", acum_sueldos, '\n')
    lista_sueldos = list(sueldos_trabajadores.values())
    media_geometrica = statistics.geometric_mean(lista_sueldos)
    print("Media geometrica: ", media_geometrica)

def ver_estadisticas(sueldos_trabajadores):
    lista_sueldos = list(sueldos_trabajadores.values())
    sueldo_mas_alto = max(lista_sueldos)
    sueldo_mas_bajo = min(lista_sueldos)
    promedio_sueldos = sum(lista_sueldos)/len(lista_sueldos)
    print("El sueldo mas bajo es: ", sueldo_mas_bajo)
    print("El sueldo mas alto es: ", sueldo_mas_alto)
    print("El sueldo promedio es: ", promedio_sueldos)
    print("")

def reporte_de_sueldos(sueldos_trabajadores):
    detalle_sueldos = []
    for trabajador, sueldo in sueldos_trabajadores.items():
        descuento_afp = sueldo*0.07
        descuento_salud = sueldo*0.12
        sueldo_liquido = sueldo - descuento_afp - descuento_salud
        trabajador = {
            "Nombre empleado": trabajador,
            "Sueldo Base": sueldo,
            "Descuento Salud": descuento_salud,
            "Descuento AFP": descuento_afp,
            "Sueldo Líquido": sueldo_liquido
        }
        detalle_sueldos.append(trabajador)
    print('{:20}{:15}{:25}{:25}{:25}'.format("Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP","Sueldo Líquido"))
    for trabajador in detalle_sueldos:
        print('{:20}{:15}{:25}{:25}{:25}'.format(trabajador["Nombre empleado"], str(trabajador["Sueldo Base"]), str(trabajador["Descuento Salud"]), str(trabajador["Descuento AFP"]), str(trabajador["Sueldo Líquido"])))

    try:
        with open("reporte_sueldos.csv", 'w', newline="" ) as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP","Sueldo Líquido"])

            for trabajador in detalle_sueldos:
                escritor.writerow([trabajador["Nombre empleado"], trabajador["Sueldo Base"], trabajador["Descuento Salud"], trabajador["Descuento AFP"], trabajador["Sueldo Líquido"]])
        print("Archivo guardado")
        
    except:
        print("Ocurrio un error al guardar el archivo de reporte de sueldos.")










