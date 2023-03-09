import pyperclip

folder_path = (
    r"C:\Users\Gero Zayas\Downloads\CODING\0 GERO PYTHON\Git-Hub Python Practice"
)

print("This is copied to clipboard! >>> chdir " + folder_path)
print("Just paste it!")

pyperclip.copy("chdir " + folder_path)

