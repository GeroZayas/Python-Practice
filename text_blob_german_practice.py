from textblob_de import TextBlobDE


# THIS IS THE TEXT
text = "Dieses Python Tutorial entsteht im Rahmen von Uni-Kursen und kann hier kostenlos genutzt werden. Python ist eine für Anfänger und Einsteiger sehr gut geeignete Programmiersprache, die später auch den Fortgeschrittenen und Profis alles bietet, was man sich beim Programmieren wünscht. Der Kurs ist eine Einführung und bietet einen guten Einstieg. Es wird aktuelles Wissen vermittelt - daher schreiben wir unseren Python-Code mit der aktuellen Python-Version 3."

blob = TextBlobDE(text)

# TAGS
print("-" * 60)
print("This is the tags: \n")
# print(blob.tags)

# WORDS
print("-" * 60)
print("This is the words: \n")
# print(blob.words)


def the_words(text=None):
    global blob
    the_len = 5
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
# print("-" * 60)
# print("This is the noun phrases: \n")
# # print(blob.noun_phrases)
# for noun_phrase in blob.noun_phrases:
#     print(
#         f"""
#           {noun_phrase}"""
#     )


# SENTENCES
print("-" * 60)
print("This is the sentences: \n")
# print(blob.sentences)

# for sentence in blob.sentences:
#     print(
#         f"""
# ----> {sentence}
#           """
#     )

# print(
#     """

#       """
# )


def the_sentiment(text=None):
    if text == None:
        text = blob
    return print(blob.sentiment)


the_sentiment()
