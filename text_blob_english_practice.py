from textblob import TextBlob

text = "Python’s iterators and iterables are two different but related tools that come in handy when you need to iterate over a data stream or container. Iterators power and control the iteration process, while iterables typically hold data that you want to iterate over one value at a time. Iterators and iterables are fundamental components of Python programming, and you’ll have to deal with them in almost all your programs. Learning how they work and how to create them is key for you as a Python developer."


# print(text)

# ----------------------------------------------------------------

blob = TextBlob(text)

# print(blob)

# ----------------------------------------------------------------
# THE TAGS


def the_tags():
    print("\nThis is TAGS:\n")

    for tag in blob.tags:
        print(
            f"""
            {tag}""",
        )


the_tags()

# ----------------------------------------------------------------

# EXTRACT VERBS AND ITS CATEGORY
verbs = ("VB", "VBG", "VBD", "VBN", "VBP")


def the_verbs():
    print("\nThis is VERBS:\n")

    for tag in blob.tags:
        if tag[1] in verbs:
            print(f" -- {tag[0]} --" + " is a " + tag[1])


the_verbs()

# ----------------------------------------------------------------

# NOUN PHRASES


def the_noun_phrases():
    print("\nThis is NOUN PHRASES:\n")

    for np in blob.noun_phrases:
        print(np)


print("-" * 60)
the_noun_phrases()


# ----------------------------------------------------------------
def the_sentences():
    print("\nThis is SENTENCES:\n")

    for sentence in blob.sentences:
        print(f"\n{sentence}")


print("-" * 60)
the_sentences()


def the_sentiment():
    print("\nThis is SENTIMENT:\n")

    # print(blob.sentiment._asdict())
    sentiment_dict = blob.sentiment._asdict()
    for k, v in sentiment_dict.items():
        # print(f"{k)} -> {v}")
        print(f"the {k} is")
        print(f"{round(v, 2)}\n")


print("-" * 60)
the_sentiment()


print("-" * 60)
# help(blob.sentiment)
