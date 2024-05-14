# coding: utf-8
from typer import Typer, run
from random import sample
from trogon import tui


app = Typer()


# This class defines two methods for generating random lottery numbers for Eurodreams and Bonoloto
# games.
class Lottery:
    def eurodreams(self):
        """
        The function generates a list of unique random numbers from a specified population range, along
        with an additional random number.
        :return: The function `eurodreams` returns a string that contains a sorted sample of 6 random
        numbers from the population range 1 to 40, along with one additional random number from the
        range 1 to 6 labeled as "sueño".
        """
        sample_size = 6
        population = range(1, 41)
        sueño = sample(range(1, 6), 1)
        unique_random_numbers_mas_sueño = (
            f"{sorted(sample(population, sample_size))}, sueño:{sueño}"
        )
        return unique_random_numbers_mas_sueño

    def bonoloto(self):
        """
        The function generates a random set of 6 unique numbers between 1 and 49 for a Bonoloto lottery
        ticket.
        :return: Numbers: [7, 15, 23, 31, 38, 45]
        """
        sample_size = 6
        population = range(1, 50)
        unique_random_numbers = sample(population, sample_size)
        return f"Numbers:{sorted(unique_random_numbers)}"


@tui
@app.command()
def eurodreams():
    lottery = Lottery()
    print(lottery.eurodreams())


@tui
@app.command()
def bonoloto():
    lottery = Lottery()
    print(lottery.bonoloto())


if __name__ == "__main__":
    run(app)
