#funciones si se elige la opcion gestion de inventario
import csv

def verificar_rol_f_v():  #veo si es farmaceutico o vendedor
    with open(r"Consigna y csv\usuarios.csv", mode='r', newline='') as file:
        reader = csv.reader(file, delimiter=';')  # Especifica el punto y coma como separador
        next(reader)  # Saltar la primera línea (encabezado)
        for row in reader:
            if row[2] == "farmaceutico" or row[2]=="vendedor":
                return True
            else:
                print("\nNo cuenta con permisos para realizar esta acción.\n")
    return False

def ingresar_stock():
    if verificar_rol_f_v:
        pass

def realizar_venta():
    pass

def seguimiento_caducidad():
    pass

