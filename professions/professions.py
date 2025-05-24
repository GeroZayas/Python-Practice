class Professions:
    def __init__(self, name: str, salary: int, experience: str, profession: str = None):
        self.name = name
        self.salary = salary
        self.experience = experience

    def __repr__(self) -> str:
        return f"Name: {self.name}\n======\nSalary: {self.salary}\n======\nExperience: {self.experience}"

    def is_working(self, working_now: bool):
        return f"{self.name} Is it working now? -> {working_now}"


class Teacher(Professions):
    def __init__(self, name: str, salary: int, experience: str, subject: str):
        super().__init__(name, salary, experience)
        self.subject = subject

    def __repr__(self) -> str:
        return super().__repr__() + f"\n======\nSubject: {self.subject}"


class EnglishTeacher(Teacher):
    def __init__(
        self, name: str, salary: int, experience: str, subject: str, certificates: str
    ):
        super().__init__(name, salary, experience, subject)
        self.certificates = certificates

    def __repr__(self) -> str:
        return super().__repr__() + f"\n======\nCertificates: {self.certificates}"


if __name__ == "__main__":
    pass
