from io import StringIO
import httpx
from rich import print


URL = "https://docs.python.org/3/library/io.html"

response = httpx.get(URL)

print(type(response.text))

f = StringIO(response.text)
