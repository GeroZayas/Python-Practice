import pyperclip
import subprocess

folder_path = (
    r"C:\Users\Gero Zayas\Downloads\CODING\0 GERO PYTHON\Git-Hub Python Practice"
)

print(f"This is copied to clipboard! >>> chdir {folder_path}")
print("Just paste it!")

pyperclip.copy(f"chdir {folder_path}")

