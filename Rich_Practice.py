# from rich.prompt import Confirm

# is_rich_great = Confirm.ask("Do you like rich?")

# assert is_rich_great

from faker import Faker 

faker = Faker()

paragraph = faker.paragraph(10) 

# MARKDOWN = f"""
# # HEllO
# {paragraph}
# ## My name is Gero
# {paragraph}
# ### I love Python!
# {paragraph}
# - 1
# - 2
# - 3 
# """

MARKDOWN = """
"""
with open("./Advanced Python Stuff.md", 'r') as file:
    MARKDOWN = file.read()


from rich.console import Console
from rich.markdown import Markdown

console = Console()
md = Markdown(MARKDOWN)
console.print(md)

print("\n\n" + "-" * 60)
input("Hit enter to quit")
