import os


# os.mkdir("my_dir_gero")

class Main:
    def __init__(self):
        pass

    root_path = (
        "/home/gero/Downloads/💻💻 CODING 💻💻/🐍🐍🐍  Gero_Python 🐍🐍🐍/Python-Practice"
    )
    directories = ["Present Simple", "Present Continuous", "Past Simple"]

    for directory in directories:
        os.mkdir(os.path.join(root_path, directory))


if __name__ = "__main__":
    pass 
