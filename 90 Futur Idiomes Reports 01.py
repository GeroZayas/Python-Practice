# Futur Idiomes Reports V -> 0.1

from docx import Document

# Create a Word file per name in list

groups = {
    "Movers L-M": [
        "Yago",
        "Etna",
        "Julia",
        "Ainhoa",
        "Paula",
        "Nicole",
        "Izan",
        "Alex",
    ],
    "Movers M-J": [
        "Facundo",
        "Judith",
        "Katerina",
        "Gerard",
        "Eric Aguado",
        "Eric Muñoz",
    ],
    "FCE L-M": ["Olivia", "Natalia", "Hannah", "Iker", "Judith", "Eva"],
    "FCE M-J": ["Gerard", "Andrea", "Hugo", "Lucia", "Kloe"],
}

for group in groups:
    for student in groups[group]:
        print(group, student)
        document = Document()

        document.add_heading(f"{student}", 0)

        document.save(f"{group}_{student}.docx")
