import os 
import time
import msvcrt
import csv
nombres=[]

with open('listado_nombres.csv',"w",newline='') as archivo_csv:
    escritor =csv.writer(archivo_csv)

    for vuelta in range(3):
        nombre=input("ingrese nombre: ")
        nombres.append(nombre)
    escritor.writerow(nombres)
