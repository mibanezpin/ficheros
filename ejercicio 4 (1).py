import requests

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

# Llamar a la función
contar_palabras_url()


