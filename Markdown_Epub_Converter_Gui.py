import PySimpleGUI as sg
import markdown
from ebooklib import epub


def create_epub(file_path, name):
    with open(file_path, "rb") as f:
        markdown_file = f.read()
        markdown_file = markdown_file.decode("utf-8", "ignore")

    html_string = markdown.markdown(markdown_file)

    book = epub.EpubBook()

    chapter = epub.EpubHtml(
        title="Hello World", file_name="hello_world.xhtml", lang="en"
    )
    chapter.content = html_string

    book.add_item(chapter)

    book.set_identifier("sample123456")
    book.set_title("Sample EPUB")
    book.set_language("en")

    book.toc = (epub.Link(epub.EpubNcx(), "ncx", "nav"),)
    book.spine = ["nav", chapter]

    epub.write_epub(f"{name}.epub", book)


layout = [
    [sg.Text("Path to file:")],
    [sg.InputText(key="file_path"), sg.FileBrowse()],
    [sg.Text("Insert name:")],
    [sg.InputText(key="name")],
    [sg.Button("Create EPUB"), sg.Button("Exit")],
]

window = sg.Window("EPUB Creator", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break

    elif event == "Create EPUB":
        file_path = values["file_path"]
        name = values["name"]
        create_epub(file_path, name)
        sg.popup("EPUB created:", f"{name}.epub")

window.close()
