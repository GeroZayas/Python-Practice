import webbrowser

look_up = input("What do you want to look up: ")

url = f"https://google.com/search?q={look_up}"
webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(
    url
)
