from itertools import combinations
from random import choice


surprises = [
    "Gain 15 Points",
    "Give 5 Points to other team",
    "Gain 10 points",
    "Lose 15 points",
    "Take 10 points from other team",
    "Everyone goes to 0 points",
    "Lose 10 points",
]

letters = ["a", "b", "c", "d", "e"]
numbers = [x for x in range(1, 6)]

letter_comb = [(l, n) for l in letters for n in numbers]

# print(letter_comb)


# FIXME It is producing surprises for the same square


def get_random_surprise_squares():
    result = []
    for s in surprises:
        the_choice = choice(letter_comb)
        result.append((the_choice, s)) if (the_choice, s) not in result else ""
    assert len(set(result)) == len(result)

    return result


# random_surprises_squares = [(choice(letter_comb), s) for s in surprises]

print(
    """
      This is random surprises squares:
      """
)

list_of_surprises = get_random_surprise_squares()

for _ in list_of_surprises:
    print(_)
