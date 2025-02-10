def guardartablamultiplicar():
    while True:
        try:
            x = int(input("Escribe un número entero entre 1 y 10: "))
            if 1 <= x <= 10:
                break
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Por favor, escribe un número válido.")
    
    nombrefichero = f"tabla-{x}.txt"
    
    with open(nombrefichero, "w") as fichero:
        for i in range(1, 11):
            fichero.write(f"{x} x {i} = {x * i}\n")
    
    print(f"Tabla de multiplicar del {x} guardada en {nombrefichero}.")

guardartablamultiplicar()

