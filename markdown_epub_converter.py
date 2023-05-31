import markdown

markdown_file = input("Epub filepath:\n >>>")

html_string = markdown.markdown(markdown_file)

from ebooklib import epub

book = epub.EpubBook()

# Add a cover image (optional)
# book.set_cover("cover.jpg", open("cover.jpg", "rb").read())

# Create an EPUB chapter
chapter = epub.EpubHtml(title="Hello World", file_name="hello_world.xhtml", lang="en")
chapter.content = html_string

# Add the chapter to the book
book.add_item(chapter)

# Define metadata
book.set_identifier("sample123456")
book.set_title("Sample EPUB")
book.set_language("en")

# Define table of contents
book.toc = (epub.Link(epub.EpubNcx(), "ncx", "nav"),)

# Define the spine
book.spine = ["nav", chapter]

# Save the EPUB file
epub.write_epub("sample.epub", book)
