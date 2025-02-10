import os
import requests

def guardar_tabla_multiplicar():
    while True:
        try:
            n = int(input("Introduce un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                break
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    nombre_fichero = f"tabla-{n}.txt"
    
    with open(nombre_fichero, "w") as fichero:
        for i in range(1, 11):
            fichero.write(f"{n} x {i} = {n * i}\n")
    
    print(f"Tabla de multiplicar del {n} guardada en {nombre_fichero}.")

def leer_tabla_multiplicar():
    while True:
        try:
            n = int(input("Introduce un número entero entre 1 y 10 para leer su tabla: "))
            if 1 <= n <= 10:
                break
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    nombre_fichero = f"tabla-{n}.txt"
    
    if os.path.exists(nombre_fichero):
        with open(nombre_fichero, "r") as fichero:
            print(fichero.read())
    else:
        print(f"El fichero {nombre_fichero} no existe.")

def leer_linea_tabla():
    while True:
        try:
            n = int(input("Introduce un número entero entre 1 y 10: "))
            m = int(input("Introduce el número de línea que deseas leer (entre 1 y 10): "))
            if 1 <= n <= 10 and 1 <= m <= 10:
                break
            else:
                print("Ambos números deben estar entre 1 y 10.")
        except ValueError:
            print("Por favor, introduce números válidos.")
    
    nombre_fichero = f"tabla-{n}.txt"
    
    if os.path.exists(nombre_fichero):
        with open(nombre_fichero, "r") as fichero:
            lineas = fichero.readlines()
            if 1 <= m <= len(lineas):
                print(lineas[m - 1].strip())
            else:
                print("La línea solicitada no existe en el fichero.")
    else:
        print(f"El fichero {nombre_fichero} no existe.")

def contar_palabras_url():
    url = "http://textfiles.com/adventure/aencounter.txt"
    try:
        response = requests.get(url)
        response.raise_for_status()
        texto = response.text
        num_palabras = len(texto.split())
        print(f"El número de palabras en el archivo es: {num_palabras}")
    except requests.exceptions.RequestException as e:
        print(f"Error al acceder al archivo: {e}")

def gestionar_listin():
    archivo = "listin.txt"
    if not os.path.exists(archivo):
        open(archivo, "w").close()
    
    def consultar_cliente(nombre):
        with open(archivo, "r") as f:
            for linea in f:
                cliente, telefono = linea.strip().split(",")
                if cliente == nombre:
                    return telefono
        return "Cliente no encontrado."
    
    def anadir_cliente(nombre, telefono):
        with open(archivo, "a") as f:
            f.write(f"{nombre},{telefono}\n")
    
    def eliminar_cliente(nombre):
        lineas = []
        with open(archivo, "r") as f:
            lineas = f.readlines()
        with open(archivo, "w") as f:
            for linea in lineas:
                if not linea.startswith(nombre + ","):
                    f.write(linea)
    
    return consultar_cliente, anadir_cliente, eliminar_cliente

consultar, anadir, eliminar = gestionar_listin()

# Ejemplo de uso
anadir("Juan", "123456789")
anadir("Maria", "987654321")
print(consultar("Juan"))
eliminar("Juan")
print(consultar("Juan"))



