import os
import requests
import csv

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

def leer_calificaciones(nombre_fichero):
    with open(nombre_fichero, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        lista_calificaciones = sorted([dict(row) for row in reader], key=lambda x: x['Apellidos'])
    return lista_calificaciones

def calcular_nota_final(lista_calificaciones):
    for alumno in lista_calificaciones:
        parcial1 = float(alumno['Parcial1'])
        parcial2 = float(alumno['Parcial2'])
        practicas = float(alumno['Practicas'])
        nota_final = (parcial1 * 0.3) + (parcial2 * 0.3) + (practicas * 0.4)
        alumno['Nota Final'] = round(nota_final, 2)
    return lista_calificaciones

def clasificar_alumnos(lista_calificaciones):
    aprobados = []
    suspensos = []
    for alumno in lista_calificaciones:
        asistencia = float(alumno['Asistencia'])
        parcial1 = float(alumno['Parcial1'])
        parcial2 = float(alumno['Parcial2'])
        practicas = float(alumno['Practicas'])
        nota_final = float(alumno['Nota Final'])
        
        if asistencia >= 75 and parcial1 >= 4 and parcial2 >= 4 and practicas >= 4 and nota_final >= 5:
            aprobados.append(alumno)
        else:
            suspensos.append(alumno)
    return aprobados, suspensos

# Ejemplo de uso
archivo_calificaciones = "calificaciones.csv"
calificaciones = leer_calificaciones(archivo_calificaciones)
calificaciones = calcular_nota_final(calificaciones)
aprobados, suspensos = clasificar_alumnos(calificaciones)

print("Aprobados:", aprobados)
print("Suspensos:", suspensos)




