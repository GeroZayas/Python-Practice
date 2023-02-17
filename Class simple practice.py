# class simple  practice

# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     def breathe(self, alive: bool = True):
#         return alive

#     def action(self, action: str):
#         return f"{self.name} is " + action


# person1 = Person("Gero", 31)

# print(person1.name, person1.age)

# person2 = Person("Mar", 31)

# print(person2.name, person2.age)

# print(person1.action("Coding"))
# print(person2.action("Doing something HHRR"))


# class Worker(Person):
#     def salary(self, salary: int):
#         return salary


# for k, v in vars(person2).items():
#     print(k + " ->", v)


class ExistMixin:
    def exist(self):
        print(f"{self.__class__.__name__} exists!")


class JumpMixin:
    def jump(self):
        print(f"{self.__class__.__name__} is jumping!")


class Dog(JumpMixin, ExistMixin):
    def __init__(self, name):
        self.name = name


my_dog = Dog("Fido")
my_dog.jump()
my_dog.exist()
