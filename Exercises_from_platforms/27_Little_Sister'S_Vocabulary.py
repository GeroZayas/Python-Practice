def add_prefix_un(word):
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """

    return "un" + word


def make_word_groups(vocab_words):
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    prefix = vocab_words[0]
    new_string = ""
    for word in vocab_words:
        if word != prefix:
            new_string += " :: " + prefix + word

    return prefix + new_string


# print(make_word_groups(['auto', 'didactic', 'graph', 'mate', 'chrome',
#       'centric', 'complete', 'echolalia', 'encoder', 'biography']))


def remove_suffix_ness(word):
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """
    # This eliminates the last four letters ness:
    root_word = word[:-4]

    # If it end in 'i' we change it to 'y'
    if root_word[-1] == "i":
        root_word = (root_word[:-1]) + "y"

    return root_word


print(remove_suffix_ness("artiness"))


def adjective_to_verb(sentence, index):
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    # This if deals with the '.' at the end, in case the index is negative, it eiminates it
    if index < 0:
        sentence = sentence[:-1]

    # We split the sentece, which makes it a list, and then we can use the index to select the word, instead just a letter, if we hadn't splited it
    sent_list = sentence.split()
    new_verb = sent_list[index] + "en"
    return new_verb
