class Human:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def show_name(self):
        print(self.name)
        return self
    
    def show_age(self):
        print(self.age)
        return self


gero = Human('Gero', 31, 'Programmer')

print(gero.show_name().show_age().show_name())