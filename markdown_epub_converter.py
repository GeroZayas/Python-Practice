import markdown

markdown_string = """
# Hello World
This is a **great** tutorial about using Markdown in ~[Python](https://python.org)~.
"""

html_string = markdown.markdown(markdown_string)
