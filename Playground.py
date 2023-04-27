class Human:
    """A class for a Human"""
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


Human.alive = "I am alive"
Human.place = 'Earth'
