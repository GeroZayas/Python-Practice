from markdown import markdown

h1 = "# My name is Gero"
p = """
And I am a future Python Expert
And I absolutely love to program every day
and solve problems.
I love my work!
"""
html1 = markdown(h1)
html2 = markdown(p)

print(html1, html2)

with open("test_md.md", "w", encoding="utf-8") as html_file:
    html_file.write(html1)
    html_file.write(html2)
