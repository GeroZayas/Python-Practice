import requests

# Hacer una solicitud GET simple
response = requests.get("https://api-english-resources.up.railway.app/resources/random")

print("Hello")

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

# get all from resources/cae
# list indices must be integers or slices, not str
response = requests.get("https://api-english-resources.up.railway.app/resources/cae")
data = response.json()
print(data)
