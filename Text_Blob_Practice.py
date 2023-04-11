from textblob import TextBlob
from collections import Counter

# https://textblob.readthedocs.io/en/dev/quickstart.html


with open("text_example.txt", "r") as text_file:
    python_text_ex = TextBlob("".join(text_file.readlines()))
    # print(python_text_ex)

text_noun_phrases = python_text_ex.noun_phrases

print("-" * 60)

print("This are the noun phrases:")
print(text_noun_phrases)

print("-" * 60)
counter = Counter(text_noun_phrases)

for element, number in counter.items():
    if number > 1:
        print(element, number)

# print(counter)

# ----------------------------------------------------------------
text_sentiment = python_text_ex.sentiment

text_words = python_text_ex.words

text_sentences = python_text_ex.sentences


print(
    f"""
      This is the sentiment of the text:
      
      {text_sentiment}
      
      These are the words of the text:
      
      {text_words}
      
      These are the sentences  of the text:
      
      {text_sentences}
      
      
      """
)

# ----------------------------------------------------------------

for sentence in text_sentences:
    print("-" * 60)
    print(sentence)
else:
    print("SUCCESS")
