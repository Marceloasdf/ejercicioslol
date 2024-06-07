
import csv
personas=[["nombre,apellido,edad"]]

from funciones_ejercicio1 import personas_agregadas


while True:
    nombre=(input("ingrese nombre: "))
    apellido=(input("ingrese apellido: "))
    edad=int(input("ingrese edad: "))
    persona=[nombre,apellido,edad]
    personas.append(persona)
    resp=(input("desea agregar otra persona(si,no)? : ")).lower()
    if resp=="no":
        print("terminando proceso")
        break
personas_agregadas(personas)

    

        