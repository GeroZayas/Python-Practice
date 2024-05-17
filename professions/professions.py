class Professions:
    def __init__(self, name: str, salary: int, experience: str, profession: str = None):
        self.name = name
        self.salary = salary
        self.experience = experience

    def __repr__(self) -> str:
        return f"Name: {self.name}, Salary: {self.salary} and Experience: {self.experience}"

    def is_working(self, working_now: bool):
        return f"{self.name} Is it working now? -> {working_now}"


if __name__ == "__main__":
    pass
