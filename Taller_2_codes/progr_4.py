class Libro:
    def __init__(self, titulo, autor, genero, año_publicacion, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año_publicacion = año_publicacion
        self.num_paginas = num_paginas
    
    def leer(self):
        print(f"Leyendo el libro '{self.titulo}'.")
    
    def prestar(self):
        print(f"El libro '{self.titulo}' ha sido prestado.")

class Casa:
    def __init__(self, direccion, num_habitaciones, num_pisos, tamaño_m2, valor_estimado):
        self.direccion = direccion
        self.num_habitaciones = num_habitaciones
        self.num_pisos = num_pisos
        self.tamaño_m2 = tamaño_m2
        self.valor_estimado = valor_estimado
    
    def cerrar_puertas(self):
        print(f"Las puertas han sido cerradas.")
    
    def cerrar_ventanas(self):
        print("El valor estimado de la casa ha sido actualizado.")

class Pelicula:
    def __init__(self, titulo, director, genero, año_estreno, duracion_minutos):
        self.titulo = titulo
        self.director = director
        self.genero = genero
        self.año_estreno = año_estreno
        self.duracion_minutos = duracion_minutos
    
    def reproducir(self):
        print(f"Reproduciendo la película '{self.titulo}'")
    
    def pausar(self):
        print(f"La película '{self.titulo}' ha sido pausada.")

class Bodega:
    def __init__(self, ubicacion, capacidad_m2, tipo_productos, temperatura, nivel_ocupacion):
        self.ubicacion = ubicacion
        self.capacidad_m2 = capacidad_m2
        self.tipo_productos = tipo_productos
        self.temperatura = temperatura
        self.nivel_ocupacion = nivel_ocupacion
    
    def verificar_disponibilidad(self, espacio_necesario):
        if espacio_necesario <= self.capacidad_m2 - self.nivel_ocupacion:
            print("Hay suficiente espacio en la bodega.")
        else:
            print("No hay suficiente espacio en la bodega.")
    
    def actualizar_ocupacion(self, nueva_ocupacion):
        self.nivel_ocupacion = nueva_ocupacion
        print("El nivel de ocupación de la bodega ha sido actualizado.")

class Lampara:
    def __init__(self, marca, color, tipo_bombilla, intensidad_luz):
        self.marca = marca
        self.color = color
        self.tipo_bombilla = tipo_bombilla
        self.intensidad_luz = intensidad_luz
        self.estado = "apagada"
    
    def encender(self):
        self.estado = "encendida"
        print("La lámpara ha sido encendida.")
    
    def apagar(self):
        self.estado = "apagada"
        print("La lámpara ha sido apagada.")

class Modem:
    def __init__(self, marca, modelo, velocidad, tipo_conexion):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.tipo_conexion = tipo_conexion
        self.estado_conexion = "desconectado"
    
    def conectar(self):
        self.estado_conexion = "conectado"
        print("El modem ha sido conectado a la red.")
    
    def desconectar(self):
        self.estado_conexion = "desconectado"
        print("El modem ha sido desconectado de la red.")

class Router:
    def __init__(self, marca, modelo, num_puertos, protocolo_comunicacion):
        self.marca = marca
        self.modelo = modelo
        self.num_puertos = num_puertos
        self.protocolo_comunicacion = protocolo_comunicacion
        self.estado = "apagado"
    
    def encender(self):
        self.estado = "encendido"
        print("El router ha sido encendido.")
    
    def apagar(self):
        self.estado = "apagado"
        print("El router ha sido apagado.")

class Maletin:
    def __init__(self, material, color, tamaño, capacidad):
        self.material = material
        self.color = color
        self.tamaño = tamaño
        self.capacidad = capacidad
        self.estado = "cerrado"
    
    def abrir(self):
        self.estado = "abierto"
        print("El maletín ha sido abierto.")
    
    def cerrar(self):
        self.estado = "cerrado"
        print("El maletín ha sido cerrado.")

class PacienteOncologico:
    def __init__(self, nombre, edad, tipo_sangre,tipo_cancer, estado_salud):
        self.nombre = nombre
        self.edad = edad
        self.tipo_sangre = tipo_sangre
        self.tipo_cancer = tipo_cancer
        self.estado_salud = estado_salud
    
    def actualizar_edad(self,nueva_edad):
        self.edad = nueva_edad
        print("La edad del paciente ha sido actualizada.")
    
    def actualizar_estado_salud(self, nuevo_estado):
        self.estado_salud = nuevo_estado
        print("El estado de salud del paciente ha sido actualizado.")

class Gato:
    def __init__(self, nombre, edad, raza, color):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.color = color
        self.estado = "despierto"
        
    def maullar(self):
        print(f"{self.nombre} dice Miau!!!")
    
    def dormir(self):
        self.estado = "dormido"
        print(f"{self.nombre} ha empezado a dormir.")