import markdown
import ebooklib


def convert_markdown_to_epub(markdown_file, epub_file):
    """Converts a Markdown file to an EPUB file.

    Args:
      markdown_file: The path to the Markdown file.
      epub_file: The path to the EPUB file.

    Returns:
      None.
    """

    # Read the Markdown file.
    markdown_content = markdown.markdown(open(markdown_file, "r").read())

    # Create an EPUB book.
    epub_book = ebooklib.epub.EpubBook()

    # Add the Markdown content to the EPUB book.
    epub_book.add_content(markdown_content)

    # Save the EPUB book.
    epub_book.write(epub_file)


if __name__ == "__main__":
    # Get the Markdown file and EPUB file paths from the command line.
    markdown_file = input("Enter the path to the Markdown file: ")
    epub_file = input("Enter the path to the EPUB file: ")

    # Convert the Markdown file to an EPUB file.
    convert_markdown_to_epub(markdown_file, epub_file)

    # Print a success message.
    print("Conversion successful!")
