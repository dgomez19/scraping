import requests

# URL de la página que quieres descargar
url = "https://www.google.com"

# Hacer la solicitud GET
response = requests.get(url)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    # Guardar el contenido en un archivo
    with open("google.html", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("Página descargada exitosamente.")
else:
    print(f"Error al descargar la página: {response.status_code}")
