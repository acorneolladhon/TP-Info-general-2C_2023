#funciones si se elige la opcion gestion de ususarios 
import csv 




def verificar_rol_a():  #veo si el usuario logueado es administrador o no 
    with open(r"Consigna y csv\usuarios.csv", mode='r', newline='') as file:
        reader = csv.reader(file, delimiter=';') 
        next(reader)  # Saltea la primera línea (encabezado)
        
        for row in reader:
            if row[2] == "administrador":
                contra_admin=row[1]
                return True
            else:
                print("\nNo cuenta con permisos necesarios para realizar esta acción.\n")
    return False


def agregar_usuario():
    if verificar_rol_a():
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        rol = input("Ingrese su rol: ")
        archivo_csv = r"Consigna y csv\usuarios.csv"

        # Verificar si el usuario ya existe en el archivo
        usuario_existente = False

        with open(archivo_csv, mode='r', newline='') as file:
            reader = csv.reader(file, delimiter=';')
            encabezado = next(reader, None)  # Lee la primera línea como encabezado

            for row in reader:
                if row and row[0] == usuario:
                    usuario_existente = True
                    break

        if usuario_existente:
            print("Usuario ya existente, no se pudo agregar el usuario.")
        else:
            with open(archivo_csv, mode='a', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow([usuario, contraseña, rol])
                print("Usuario", usuario, "agregado con éxito!")


def eliminar_usuario():
    if verificar_rol_a():
        pass
        

def cambiar_contraseña():
    pass



    