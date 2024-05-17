"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
"""


def spin_words(sentence):
    final_sentence = ""
    # We split the sentece so we can loop over the words
    sent_splt = sentence.split()

    # If the word is 5 or more letters long then we reverse it
    #  We reverse it with word[::-1]
    for w in sent_splt:
        if len(w) >= 5:
            w = w[::-1]
            # We added to our var final_sentence, which we will return
            final_sentence += w + " "
        else:
            final_sentence += w + " "
    # Note the .strip() method at the end, so we don't have another space ' ' at the end of string
    return final_sentence.strip()


# Testing:
print(spin_words("Hey fellow warriors"))
print(spin_words("This is a test"))
print(spin_words("This is another test"))
