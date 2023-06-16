from textblob import TextBlob

text = """LONDON -- A delegation of African leaders has arrived in Ukraine, kicking off the African Peace Initiative Mission in a bid to find a peaceful resolution to the war in Ukraine.

The mission is headed by South African President Cyril Ramaphosa and comprised of leaders from Egypt, Senegal, Zambia and the Comoros.

Uganda’s president, Yoweri Museveni, was due to join the delegation but had to bow out after testing positive for COVID. Uganda’s special envoy for special duties will now represent the East African nation.

This is the first foreign delegation to meet with leaders of both Ukraine and Russia. Jean-Yves Olliver, a French businessman with a long history in peace negotiations in Africa, helped assemble the delegation.

The delegation is also expected to discuss continued grain exports and the shipment of Russian fertilizers to help alleviate food insecurity on the continent. Up to 20 million people in the Horn of Africa could go hungry this year.

"The African Peace Mission brings an African perspective and an appeal for a peace process to deliberations that are underway in various parts of the world and within different formations of nations on how to address the conflict in Ukraine and Russia," Ramaphosa said on the eve of the mission.

He added, "This peace initiative should be seen as completing other peace initiatives that other parties have put forward. The strength of this mission is that African leaders will be engaging with both parties."""


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
    """
    It prints the sentiment of the text.
    """
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
