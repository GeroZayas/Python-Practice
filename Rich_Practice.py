# from rich.prompt import Confirm

# is_rich_great = Confirm.ask("Do you like rich?")

# assert is_rich_great

MARKDOWN = """
# This is an h1

Rich can do a pretty *decent* job of rendering markdown.

1. This is a list item
2. This is another list item
"""
from rich.console import Console
from rich.markdown import Markdown

console = Console()
md = Markdown(MARKDOWN)
console.print(md)

print("\n\n" + "-" * 60)
input("Hit enter to quit")
