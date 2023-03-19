# 97 practicing with files and os.py
import os


def create_files(folder_path: str, extension: str, amount_of_files: int):
    """
    Creates a number files with a determined extension
    """
    file_name = "example_name"
    counter = 0
    for i in range(amount_of_files):
        counter += 1
        try:
            with open(f"{folder_path}/{counter} {file_name}.{extension}", "x"):
                print("done")
        except FileExistsError:
            print("File already exists")


create_files(
    folder_path="./test_folder_long_names/", extension="txt", amount_of_files=5
)


list_of_files = os.listdir("./test_folder_long_names")

print(list_of_files)

counter: int = 0


def shorten_name_files(files_list: list, length_of_name: int):
    for filename in list_of_files:
        # print(len(filename))
        the_counter = 0
        if len(filename) > length_of_name:
            try:
                os.rename(
                    f"./test_folder_long_names/{filename}", filename[:length_of_name]
                )
            except Exception:
                the_counter += 1
                os.rename(
                    f"./test_folder_long_names/{filename}",
                    f"{the_counter}-{filename[:length_of_name]}",
                )


shorten_name_files(files_list=list_of_files, length_of_name=3)
