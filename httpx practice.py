import httpx

response = httpx.get("https://www.azlyrics.com/lyrics/loony/beg.html")

print("Response's status code:\n->", response.status_code)

print("Response's headers:\n->", response.headers)


