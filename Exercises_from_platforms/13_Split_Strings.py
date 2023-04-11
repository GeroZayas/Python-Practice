"""Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd
number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""


def solution(s: str) -> list:
    # We declare the var list we will return
    list_of_letter_pairs = []
    # We add '_' in case the string's len is odd, so we still have a pair
    if len(s) % 2 != 0:
        s += '_'
    # We declare two vars for indexes to move iterate through the given string
    index_1 = 0
    index_2 = 2
    # We set the range to half (/2) as our final list of pairs will be half the len of our argument string given
    # Note that we make an integer (int(len(s)/2)) as we cannot have a float here for the range to work
    for letter in range(int(len(s) / 2)):
        # We append to the list the new pairs of letters
        list_of_letter_pairs.append(s[index_1:index_2])
        # We increase indexes by 2 to get hold of the next pair on the next iteration
        index_1 += 2
        index_2 += 2
    return list_of_letter_pairs


print(solution('abc'))  # ['ab', 'c_']
print(solution('abcdef'))  # ['ab', 'cd', 'ef']
