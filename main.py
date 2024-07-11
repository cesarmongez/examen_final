import funciones as fn

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

sueldos_trabajadores = {trabajador:0 for trabajador in trabajadores}
while True:
    try:
        print("***********MENU***********")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas.")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        opcionMenu = int(input("Ingrese una opción: "))

        if opcionMenu == 1:
            sueldos_trabajadores = fn.asignar_sueldos_aleatorios(trabajadores)
            print("Sueldos asignados correctamente.")
        elif opcionMenu == 2:
            fn.clasificar_sueldos(sueldos_trabajadores)
        elif opcionMenu == 3: 
            fn.ver_estadisticas(sueldos_trabajadores)
        elif opcionMenu == 4: 
            fn.reporte_de_sueldos(sueldos_trabajadores)
        elif opcionMenu == 5: 
            print("Finalizando programa…")
            print("Desarrollado por César Mongez)")
            print("RUT 26.579.154-9")
        else:
            print("Por favor, seleccione una opción válida.")

    except ValueError:
        print("Por favor, ingrese solo números ")
    except Exception as e:
        print(e)
    except:
        print("Ocurrio un error inesperado.")
        