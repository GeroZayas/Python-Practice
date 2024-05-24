class Gero:
    def __init__(self, name, age, work):
        self.name = name
        self.age = age
        self.work = work

    def go_workout(self):
        print(f"{self.name} is going to workout.")

    def study_programming(self):
        print(f"{self.name} is studying programming.")

    def __repr__(self):
        return f"Gero(name='{self.name}', age={self.age}, work='{self.work}')"


if __name__ == "__main__":
    pass
