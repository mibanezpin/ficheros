import os
import requests
import csv
import pandas as pd

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

def obtener_pib_pais():
    url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open("pib.tsv", "wb") as file:
            file.write(response.content)
        
        df = pd.read_csv("pib.tsv", sep="\t")
        pais = input("Introduce las iniciales del país (ejemplo: ES para España): ").upper()
        
        for index, row in df.iterrows():
            if row["unit,geo\time"][-2:] == pais:
                print(row)
    except requests.exceptions.RequestException as e:
        print(f"Error al acceder al archivo: {e}")


obtener_pib_pais()




