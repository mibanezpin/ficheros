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
            print("Introduce un número válido.")
    
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
            print("Introduce un número válido.")
    
    nombre_fichero = f"tabla-{n}.txt"
    
    if os.path.exists(nombre_fichero):
        with open(nombre_fichero, "r") as fichero:
            print(fichero.read())
    else:
        print(f"El fichero {nombre_fichero} no existe.")

guardartablamultiplicar()
leertablamultiplicar()

