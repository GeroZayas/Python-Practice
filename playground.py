import requests

# Hacer una solicitud GET simple
response = requests.get(
    "https://api-english-resources.up.railway.app/resources/random",
)

# Verificar el estado de la respuesta
if response.status_code == 200:
    # Procesar los datos JSON
    data = response.json()
    for e in data:
        print(
            f"""
        {e} \t\t-> {data[e]}
        """
        )
else:
    print(f"Error: {response.status_code}")

# Hacer una solicitud POST con datos
# payload = {"key": "value"}
# response = requests.post("https://api.example.com/post", data=payload)
