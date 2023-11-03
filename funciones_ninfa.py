# def agregardatos(listanombres,listalegajos,listanotas) :
#     nombre=input('Ingrese el nombre del estudiante')
#     legajo=input('Ingrese el legajo del estudiante')
#     nota=input('ingrese nota')
#     listanombres.append(nombre)
#     listalegajos.append(legajo)
#     listanotas.append(nota)  

# def escribirarchivo(file,listanombres,listalegajos,listanotas):
#     with open(file,'w',newline='',encoding='utf8') as archivo:
#         escritor=csv.writer(archivo)
#         for i in range(len(listanombres)):
#             escritor.writerow([listanombres[i],listalegajos[i],listanotas[i]])
#     archivo.close()

# def crearlista(file):
#     nombrealum=[]
#     legajoalum=[]
#     notasalum=[]
#     try:
#         with open(file,'r',encoding='utf8') as archivo:
#             lector=csv.reader(archivo)
#             for line in lector:
#                 print(line)
#                 nombrealum.append(line[0])
#                 legajoalum.append(line[1])
#                 notasalum.append(line[2])
        
#             return nombrealum,legajoalum,notasalum

#     except FileNotFoundError:
#         print("El archivo no existe o no esta ubicado donde lo estas buscando")

# # def leerarchivoread(file):
# #     try:
# #         with open(file,'r',encoding='utf8') as archivo:
# #             lector=csv.reader(archivo)

# #     except:
# #         print("El archivo no existe o no esta ubicado donde lo estas buscando")
