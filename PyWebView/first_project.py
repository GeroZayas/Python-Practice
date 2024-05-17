import webview
from enum import Enum


class Names(Enum):
    MAR = 1
    GERO = 2
    ELISA = 3


html = "<h2>HELLO</h2>"

webview.create_window(
    title="First Project Gero",
    background_color="#fcba03",
    draggable=False,
    resizable=False,
    height=500,
    width=500,
    shadow=True,
    html=html,
)

webview.screens

webview.start()
