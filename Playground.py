# The class `Professions` in Python defines attributes for name, salary, and experience of a
# profession.
from professions.professions import Professions, Teacher, EnglishTeacher
from gero_new_python_file import Gero

firefighter = Professions("Firefighter", 24000, "A lot")

print(firefighter)

answer = firefighter.is_working(False)

print(answer)

teacher = Teacher(name="Elisa", salary=30000, experience="Lots", subject="Medicine")
print(teacher)
print(teacher.is_working(True))


english_teacher = EnglishTeacher(
    name="Gerardito",
    subject="ESL",
    experience="Many years",
    certificates="CAE - ADVANCED",
    salary=45000,
)


print(english_teacher)


new_gero_instance = Gero("Gero The Second", age=23, work="Python")
print(new_gero_instance)
