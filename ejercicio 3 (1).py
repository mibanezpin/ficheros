import os

def guardartablamultiplicar():
    while True:
        try:
            n = int(input("Escribe un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                break
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Escribe un número válido.")
    
    nombre_fichero = f"tabla-{n}.txt"
    
    with open(nombre_fichero, "w") as fichero:
        for i in range(1, 11):
            fichero.write(f"{n} x {i} = {n * i}\n")
    
    print(f"Tabla de multiplicar del {n} guardada en {nombre_fichero}.")

def leertablamultiplicar():
    while True:
        try:
            n = int(input("Escribe un número entero entre 1 y 10 para leer su tabla: "))
            if 1 <= n <= 10:
                break
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Escribe un número válido.")
    
    nombre_fichero = f"tabla-{n}.txt"
    
    if os.path.exists(nombre_fichero):
        with open(nombre_fichero, "r") as fichero:
            print(fichero.read())
    else:
        print(f"El fichero {nombre_fichero} no existe.")

def leerlineatabla():
    while True:
        try:
            n = int(input("Escribe un número entero entre 1 y 10: "))
            m = int(input("Escribe el número de línea que deseas leer (entre 1 y 10): "))
            if 1 <= n <= 10 and 1 <= m <= 10:
                break
            else:
                print("Los dos números deben estar entre 1 y 10.")
        except ValueError:
            print("Escribe números válidos.")
    
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

guardartablamultiplicar()
leertablamultiplicar()
leerlineatabla()


