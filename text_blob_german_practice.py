import os
from enum import Enum

os.system("cls")


from textblob_de import TextBlobDE


# THIS IS THE TEXT
text = "Bei Python spricht man von einer Skriptsprache -  ein erstelltes Programm wird interpretiert, wenn es gestartet wird. Daher bekommt man erst dann Fehlermeldungen, wenn Fehler im Python-Programm sind. Dazu aber später mehr. Die Sprache ist sehr einfach zu lernen und durch die (erzwungene) saubere Erstellung von Code punktet die Sprache: Sie ist gut lesbar und hat einen übersichtlichen kurzen Code. Daher ist Python sehr einfach zu lernen und ideal als Einführung in eine Programmiersprache. Viel Spaß in diesem Python Kurs. "

blob = TextBlobDE(text)


class Category(Enum):
    VERB = "VB"
    PAST_TENSE_VERB = "VBD"
    GER_PRESENT_PART = "VBG"
    PAST_PART = "VBN"


# TAGS
print("-" * 60)
print("This is the tags: \n")
# print(blob.tags)


def the_tags():
    for tag in blob.tags:
        print(
            f"""
{' - '.join(tag)}"""
        )


# the_tags()


# categories = ("VB", "VBN", "MD")
categories = ()
for tag in blob.tags:
    if tag[1] in categories:
        print(tag[0] + " is a " + tag[1])


# WORDS
print("-" * 60)
print("This is the words: \n")
# print(blob.words)


def the_words(text=None):
    global blob
    the_len = 0
    if text == None:
        text = blob

    for word in blob.words:
        if len(word) > the_len:
            print(
                f"""
        ---> {word}"""
            )


# the_words()

# # NOUN PHRASES
print("-" * 60)
print("This is the noun phrases: \n")
# print(blob.noun_phrases)


def the_noun_phrases():
    for noun_phrase in blob.noun_phrases:
        print(
            f"""
            {noun_phrase}"""
        )


# the_noun_phrases()


# SENTENCES
print("-" * 60)
print("This is the sentences: \n")
# print(blob.sentences)


def the_sentences():
    for sentence in blob.sentences:
        print(
            f"""
    ----> {sentence}
            """
        )

    print(
        """

        """
    )


# the_sentences()


def the_sentiment(text=None):
    if text == None:
        text = blob
    return print(blob.sentiment)


print("-" * 60)
print("\nThe sentiment:\n")
the_sentiment()
