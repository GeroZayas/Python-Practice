from dataclasses import dataclass


@dataclass
class Being:
    def __init__(self, species):
        self.species = species

    def breathe(self):
        return "I breathe"

    def die(self, alive: bool = True):
        return f"Am I alive? -> {alive}"

    def reason(self, reasonable):
        return reasonable


class HumanBeing(Being):
    def __init__(self, species):
        super().__init__(species)
        self.reason(reasonable=True)


class Animal(Being):
    def __init__(self, species):
        super().__init__(species)
        self.reason(reasonable=False)


dog = Animal(species="Dog")

person = HumanBeing(species="Human")

print(f"dog -> {dog.die(alive=False)}")
print(f"person -> {person.die()}")
