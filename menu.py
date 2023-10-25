comenzar=True
while comenzar==True:
    opcion=int(input(("""¿Qué desea realizar?
                1- Gestión de usuarios
                2- Gestión de inventario
                3- Informes
                4- Salir
                Opción: """)))
    
    if opcion==1:
        opcion_gest_usu=int(input("""\n¿Qué desea realizar?
                1-Agregar usuario
                2-Eliminar usuario
                3-Cambiar contraseña
                4-Volver al menu principal
                Opción: """))
        
        # elif choice_empleado=="5":
        #             break

        #         else:
        #             print("La opción ingresada no es válida.")
    
    elif opcion==2:
        opcion_gest_inv=int(input("""\n¿Qué desea realizar?
                1-Ingresar nuevo stock
                2-Realizar una venta
                3-Seguimiento de caducidad
                4-Volver al menu principal
                Opción: """))
    
    elif opcion==3:
        opcion_inventario=int(input("""\n¿Qué desea realizar?
                1-Ranking de ventas por proveedor
                2-Promedio de diferencia entre fecha de venta y fecha de vencimiento
                3-Informe de productos vencidos
                4-Volver al menu principal
                Opción: """))
        
    elif opcion==4:
        break

