# install prettytable module
import prettytable as pt

# get random words from faker module
import faker

# 20 words from faker module
def get_names(num_words):
    return [faker.Faker().name() for _ in range(num_words)]

# print(get_words(20))

# function gent random ages from 1 to 100
def get_age(num):
    return [faker.Faker().random_int(min=1, max=100) for _ in range(num)]

# print(get_age(20))

# put the two lists together
ages_names = list(zip(get_names(20), get_age(20)))

print(ages_names)