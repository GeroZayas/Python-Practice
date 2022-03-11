import platform as pl


# Using iter() and next()
new_tuple = ("gero", "gupa", "camtu")

my_iterator = iter(new_tuple)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# Getting information from Python Modules with dir()
x = dir(iter)
print(x)

# Using module platform to get info about the system and more
sys_info = pl.system(), pl.architecture(), pl.python_version_tuple()  # ('Windows', ('64bit', 'WindowsPE'), ('3', '10', '2'))
print(sys_info)

