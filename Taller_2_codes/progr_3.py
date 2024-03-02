def comparar_cadenas(cadena):
    return len(cadena) % 2, cadena

def ordenar_cadenas(lista_cadenas, ruta):
    lista_cadenas.sort(key=comparar_cadenas)
    with open(ruta, "w") as archivo:
        for cadena in lista_cadenas:
            archivo.write(cadena + "\n")

lista = ["hola", "oso", "perro", "gato", "elefante", "tigre", "ardilla", "pato", "caballo", "abeja", "jirafa", "koala", "serpiente", "tortuga", "iguana"]
ruta = "C:\\Users\\carmo\\OneDrive\\Escritorio\\Semestre7\\Progra_IV\\Taller_2_codes\\arch_3.txt"

ordenar_cadenas(lista, ruta)
with open(ruta, "r") as archivo:
    print(archivo.read())


