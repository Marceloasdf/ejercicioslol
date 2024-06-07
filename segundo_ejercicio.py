import csv

personas=[]


for vuelta in range(3):
    nombre=input("ingrese nombre: ")
    apellido=input("ingrese apellido: ")
    persona = [nombre,apellido]
    personas.append(persona)

with open("listado_nombreapelido.csv",'w',newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(personas)