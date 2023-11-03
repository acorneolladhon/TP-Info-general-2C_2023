import csv

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

def posicion():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    archivo_csv = r"Consigna y csv\usuarios.csv"  # Ruta del archivo CSV

    posicion = encontrar_usuario_y_contraseña(usuario, contraseña, archivo_csv)
    if posicion is not None:
        print("Usuario y contraseña encontrados en la fila",posicion, "del archivo.")
    else:
        print("Usuario y contraseña no encontrados en el archivo.")


posicion()


