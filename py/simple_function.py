class ProgrammingLanguage:
    def __init__(self, name: str, version: str):
        self.name = name
        self.version = "1.0"

    def __str__(self):
        return self.name + " version " + self.version


def simple_function(a: int, b: str) -> str:
    return str(a) + b


print("This is a simple function")

print(simple_function(1, "test"))


python = ProgrammingLanguage("Python", "3.10")
