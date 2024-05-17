# The class `Professions` in Python defines attributes for name, salary, and experience of a
# profession.
from professions.professions import Professions

teacher = Professions("Teacher", 24000, "A lot")

print(teacher)

answer = teacher.is_working(False)

print(answer)
