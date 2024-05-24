class Gero:
    def __init__(self, name, age, work):
        self.name = name
        self.age = age
        self.work = work

    def go_workout(self):
        print(f"{self.name} is going to workout.")

    def study_programming(self):
        print(f"{self.name} is studying programming.")


gero = Gero(name="Gero", age=32, work="programmer")

print(gero)
