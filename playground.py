class Human:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def works(self, work: bool):
        return "Yes, I work" if work else "No, I dont"


class Engineer(Human):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)

    def works(self):
        return "Always working"


gero = Engineer(name="Gero", age=32)

mar = Human("Mar", 28)

print("This is Gero")
print(gero.name, gero.age, gero.works())

print("This is Mar")
print(mar.name, mar.age, mar.works(False))
