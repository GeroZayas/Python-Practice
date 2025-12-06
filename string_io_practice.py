from rich import print, print_json
from httpx import Client, AsyncClient
from io import StringIO

client = Client()

response = client.get("https://api-english-resources.up.railway.app/resources/random")

if response.status_code == 200:
    content = response.text
else:
    print("Something went wrong")
    print(response.status_code)

# CREATE A BUFFER
random_resource_buffer = StringIO(content)

print_json(random_resource_buffer.read())

response = client.get("https://api-english-resources.up.railway.app/resources/random")

if response.status_code == 200:
    content = response.text
else:
    print("Something went wrong")
    print(response.status_code)

random_resource_buffer.write(content)

print("After adding more".center(80,"-"))
random_resource_buffer.seek(0)
print(random_resource_buffer.read())

random_resource_buffer.seek(0)
with open("new_file_random_api_english_stuff.txt", "w") as file:
    file.writelines(random_resource_buffer)
    
    