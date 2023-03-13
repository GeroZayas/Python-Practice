from textblob import TextBlob

text = "Generating realistic location data for users for testing or modeling simulations is a hard problem. Current approaches just create random locations inside a box, placing users in waterways or on top of buildings. This inability to make accurate, synthetic location data stifles a lot of innovative projects that require diverse and complex datasets to fuel their work."


# print(text)

# ----------------------------------------------------------------

# Creating a TextBlob object.
blob = TextBlob(text)

# print(blob)

# ----------------------------------------------------------------
# THE TAGS


def the_tags():
    """
    It prints the tags of the text.
    """
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
    """
    This function prints out the verbs in the text
    """
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
