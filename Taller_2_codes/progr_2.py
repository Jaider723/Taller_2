import os

class Usuario:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        
def contar_repetidos(usuarios, elemento):
    contador = 0 
    for usuario in usuarios:
        if elemento == usuario.nombre:
            contador += 1
    
    with open(ruta, "w") as archivo:
        archivo.write(f"Usuario: {elemento}\n")
        archivo.write(f"Número de apariciones: {contador}, ")
        if contador % 2 == 0:
            archivo.write("Entonces la cantidad es par.\n")
        else:
            archivo.write("Entonces la cantidad es impar.\n")

ruta = "C:\\Users\\carmo\\OneDrive\\Escritorio\\Semestre7\\Progra_IV\\Taller_2_codes\\arch_2.txt"
usuarios = [Usuario("Juan", 26, "Médico"), Usuario("María", 23, "Enfermera"), Usuario("Juan", 26, "Médico"), Usuario("David", 20, "Auxiliar"), Usuario("María", 23, "Enfermera")]
contar_repetidos(usuarios,"Juan")
with open(ruta, "r") as archivo:
    print(archivo.read())
