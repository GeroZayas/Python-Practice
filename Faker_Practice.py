# import click
# from trogon import tui


# # install prettytable module

# # get random words from faker module
# import faker


# # 20 names from faker module
# @tui()
# @click.command()
# @click.option("-a", default=5, help="Number of fake names.")
# def names(a):
#     "Gives a list of x amount of fake names"
#     result = [faker.Faker().name() for _ in range(int(a))]
#     print(result)


# # print(get_words(20))


# @tui()
# @click.command()
# @click.option("-a", default=5, help="Number of random words.")
# def words(a):
#     "Gives a list of x amount of random words"
#     result = [faker.Faker().word() for _ in range(int(a))]
#     print(result)


# if __name__ == "__main__":
#     names()
#     words()

#     # print(get_age(20))

#     # put the two lists together
#     # ages_names = list(zip(get_names(20), get_age(20)))

#     # print(ages_names)


import click
import faker
from trogon import tui


@tui()
@click.command()
@click.option("-n", "--names", default=5, help="Number of fake names.")
@click.option("-w", "--words", default=5, help="Number of random words.")
def generate_data(names, words):
    "Generates fake names and random words."
    fake_names = [faker.Faker().name() for _ in range(int(names))]
    fake_words = [faker.Faker().word() for _ in range(int(words))]

    print("Fake Names:", fake_names)
    print("---------------------------------------------------------")
    print("Random Words:", fake_words)


if __name__ == "__main__":
    generate_data()
