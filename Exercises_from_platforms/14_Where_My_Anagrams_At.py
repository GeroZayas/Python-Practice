"""
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false

Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an
array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""


def anagrams(word: str, words: list) -> list:
    # We declare the list var that we will return
    anagram_list = []

    # For words to be anagrams: they need to have the same len and the same letters
    # we iterate over words list (given as arg)
    for w in words:
        # we check if they have the same len and the letters
        # Note how we use sorted() -> if after being sorted they are identical: they have the same letters
        if len(w) == len(word) and sorted(w) == sorted(word):
            anagram_list.append(w)
    return anagram_list


print(anagrams("abba", ["aabb", "abcd", "bbaa", "dada"]))  # => ['aabb', 'bbaa']
print(
    anagrams("racer", ["crazer", "carer", "racar", "caers", "racer"])
)  # => ['carer', 'racer']
print(anagrams("laser", ["lazing", "lazy", "lacer"]))  # => []
