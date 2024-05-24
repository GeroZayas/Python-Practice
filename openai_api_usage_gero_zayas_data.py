import requests

# URL of the webpage to access
url = "https://platform.openai.com/organization/usage"

# Google login credentials
email = "gerozayas@gmail.com"
password = "Clavegerozayas7"

# Create a session
session = requests.Session()

# Perform login with Google
login_data = {"email": email, "password": password}
session.post("https://accounts.google.com/signin/v2/identifier", data=login_data)

# Access the OpenAI usage page
response = session.get(url)

# Check if the connection was successful
if response.status_code == 200:
    print("Connection successful")
else:
    print("Connection failed")
