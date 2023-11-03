import csv
from menu import *

#desde aca se inicia el programa

# with open(r"Consigna y csv\usuarios.csv", mode='r', newline='') as file:
#     reader = csv.reader(file, delimiter=';')  # Especifica el punto y coma como separador
#     next(reader)  # Saltar la primera línea (encabezado)
#     for row in reader:
#         print(row[0], row[1], row[2])
        

def verificar_inicio_sesion(usuario, contraseña):
    with open(r"Consigna y csv\usuarios.csv", mode='r', newline='') as file:
        reader = csv.reader(file, delimiter=';')  # Especifica el punto y coma como separador
        next(reader)  # Saltar la primera línea (encabezado)
        for row in reader:
            if row[0] == usuario and row[1] == contraseña:
                return True
    return False

def encontrar_usuario_y_contraseña(usuario, contraseña, archivo_csv):
    posicion = None
    contador = 0

    with open(archivo_csv, mode='r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Saltar la primera línea (encabezado)

        for row in reader:
            contador += 1
            if len(row) >= 2 and row[0] == usuario and row[1] == contraseña:
                # Se encontró una coincidencia
                posicion = contador
                break

    return posicion

def iniciar_sesion():
    archivo=r"Consigna y csv\usuarios.csv"
    inicio = False
    while not inicio:  #mientras incio sea flase
        usuario_inicio = input("Nombre de usuario: ")
        contraseña_inicio = input("Contraseña: ")
        if verificar_inicio_sesion(usuario_inicio, contraseña_inicio):
            print("Inicio de sesión exitoso.")
            inicio = True
            main()
        else:
            print("\nUsuario o contraseña incorrectos. Inténtelo de nuevo.\n")
        posicion=encontrar_usuario_y_contraseña(usuario_inicio,contraseña_inicio,archivo)
        if posicion is not None:
            print("Usuario y contraseña encontrados en la fila",posicion, "del archivo.")
        else:
            print("Usuario y contraseña no encontrados en el archivo.")

    return usuario_inicio, contraseña_inicio, posicion

iniciar_sesion()

