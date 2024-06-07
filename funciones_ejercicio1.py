import csv
def nombre_mas_largo(p_lista):
    for x in range(3):
        if x==0:
            nombre_largo = p_lista[0]
        else:
            len(p_lista[x]> len(nombre_largo))
            nombre_largo = p_lista[x]
    print("el nombre mas largo es: ",nombre_largo)


def almacenar_datos(p_personas):
    with open("listado_nombreapelido.csv",'w',newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(p_personas)