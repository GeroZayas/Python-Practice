import azapi

API = azapi.AZlyrics("duckduckgo", accuracy=0.5)

artist = input("Insert Artist:\n>>> ")
title = input("Insert Song Title:\n>>> ")


API.artist = artist
API.title = title

API.getLyrics(save=True, ext="lrc")

print(API.lyrics)

# Correct Artist and Title are updated from webpage
print(API.title, API.artist)
