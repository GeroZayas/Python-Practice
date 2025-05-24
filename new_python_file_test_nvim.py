import collections

Programmer = collections.namedtuple(
    "Programmer", ["name age favorite_lang years_exp"], defaults="Python"
)
