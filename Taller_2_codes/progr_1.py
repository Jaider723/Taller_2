import os

def get_numeros(numeros):
    numero=int(input("Ingrese un número de 2 cifras: "))
    if numero>9 and numero<100:
        numeros.append(numero)
    else: 
        print("El número ingresado no es de 2 cifras.")
        get_numeros(numeros)
        
def suma_digitos(numeros):
    sumaDigitos=[]
    for numero in numeros:
        suma=numero//10 + numero%10
        sumaDigitos.append(str(suma) + "\n")
    with open(ruta, "w") as archivo:
        archivo.writelines(sumaDigitos)
 
ruta = "C:\\Users\\carmo\\OneDrive\\Escritorio\\Semestre7\\Progra_IV\\Taller_2_codes\\arch_1.txt"
numeros=[]
largo=int(input("Ingrese el largo de la lista: "))
for i in range(largo):
    get_numeros(numeros)
sumaDigitos=suma_digitos(numeros)
print(numeros)
with open(ruta, "r") as archivo:
    print(archivo.readlines())