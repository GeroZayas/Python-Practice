import os

"""
This simple program 
a) changes spaces in the name of files to underscores.
b) capitalizes every word in the name -> CamelCase

ex. "file number 1" -> "File_Number_1"
"""

# Get path
currect_folder = os.getcwd()
print(currect_folder)


files_and_directories = os.listdir(currect_folder)
# print(files_and_directories)


def new_name_undescored(old_name):
    words = old_name.split()
    return "_".join(words).title()


extension = input(
    """What type of files do you want to change?
Insert extension here (ex. "py", "txt"): 
"""
)

counter = 0
for file in files_and_directories:
    if file.endswith(f".{extension}"):
        os.rename(file, new_name_undescored(file))
        counter += 1

if counter > 0:
    print(f"DONE in {counter} files!")
else:
    print("No files with that extension found!")
