import os

"""
This simple program 
a) changes spaces in the name of files to underscores.
b) capitalizes every word in the name

ex. "file number 1" -> "File_Number_1"
"""

# Getting the current working directory.
current_folder = os.getcwd()
print(current_folder)


files_and_directories = os.listdir(current_folder)
# print(files_and_directories)


def new_name_undescored(old_name):
    name, extension = old_name.split(".")
    name = name.replace(" ", "_")
    return f"{name.title()}.{extension}"


# IF NAME STARTS WITH DIGITS, DELETE TE NUMBERS
# ----------------------------------------------------------------
def eliminate_digits_at_beginning_of_name(file_name):
    if file_name[0].isdigit():
        for e in file_name:
            if e.isdigit():
                file_name = file_name.replace(e, "")
    print("file_name: ", file_name)

    new_file_name = ""

    if file_name.startswith("_"):
        new_file_name = file_name[1:]
        print("new_file_name : ", new_file_name)

    return new_file_name


# ----------------------------------------------------------------

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

for file in files_and_directories:
    if file.endswith(f".{extension}"):
        try:
            os.rename(file, eliminate_digits_at_beginning_of_name(file))
<<<<<<< HEAD
        except Exception as e:
            print("Exception: ", e)
            os.rename(file, f"Different {eliminate_digits_at_beginning_of_name(file)}")
=======
        except Exception:
            print("Exception: ", Exception)
>>>>>>> 3237ed435c02484fe3ee86c30bdde2cb797e9240
        finally:
            continue


if counter > 0:
    print(f"DONE in {counter} files!")
else:
    print("No files with that extension found!")
