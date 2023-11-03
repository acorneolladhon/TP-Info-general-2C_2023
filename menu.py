import csv
# from gestion_inventario import verificar_rol_f_v, ingresar_stock, realizar_venta, seguimiento_caducidad
# from gestion_usuarios import agregar_usuario, eliminar_usuario, cambiar_contraseña
# from informes import ranking_ventas_proveedor, diferencia_venta_vencimiento, informe_prod_vencidos
from gestion_usuarios import *
from gestion_inventario import *
from informes import  *


def obteneropcion(mensaje):
    validasopciones=['1','2','3','4']
    opcion=input(mensaje)
    while(opcion not in validasopciones):
            opcion=input('\nERROR\n' + mensaje)
    return opcion

 
def menu(mensaje):
    opcion=obteneropcion(mensaje)
    while opcion!='4':
        if opcion=="1":
            opcion_gest_usu=int(input("""\n¿Qué desea realizar?
                    1-Agregar usuario
                    2-Eliminar usuario
                    3-Cambiar contraseña
                    4-Volver al menu principal
                    Opción: """))
            if opcion_gest_usu==1:
                 agregar_usuario()
            elif opcion_gest_usu==2:
                 eliminar_usuario()
            elif opcion_gest_usu==3:
                 cambiar_contraseña()
            elif opcion_gest_usu==4:
                 pass
            

        elif opcion=="2":
            if verificar_rol_f_v==True: #solo se puede acceder si se cumple esto
               opcion_gest_inv=int(input("""\n¿Qué desea realizar?
                         1-Ingresar nuevo stock
                         2-Realizar una venta
                         3-Seguimiento de caducidad
                         4-Volver al menu principal
                         Opción: """))
               if opcion_gest_inv==1:
                    ingresar_stock()
               elif opcion_gest_inv==2:
                    realizar_venta()
               elif opcion_gest_inv==3:
                    seguimiento_caducidad()
               elif opcion_gest_inv==4:
                    pass
            else:
                 print("No cuenta con los permisos necesarios par realizar esta accion.")

        elif opcion=="3":
            opcion_inventario=int(input("""\n¿Qué desea realizar?
                    1-Ranking de ventas por proveedor
                    2-Promedio de diferencia entre fecha de venta y fecha de vencimiento
                    3-Informe de productos vencidos
                    4-Volver al menu principal
                    Opción: """))
            if opcion_inventario==1:
                 ranking_ventas_proveedor()
            elif opcion_inventario==2:
                 diferencia_venta_vencimiento()
            elif opcion_inventario==3:
                 informe_prod_vencidos()
            elif opcion_inventario==4:
                 pass

        opcion=obteneropcion(mensaje)
    

def main():
     mensaje= """¿Qué desea realizar?
                    1- Gestión de usuarios
                    2- Gestión de inventario
                    3- Informes
                    4- Salir
                    Opción:  """  
     menu(mensaje) 
        

