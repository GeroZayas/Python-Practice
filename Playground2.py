import nltk

# read in the text file
with open('notes.txt', 'r') as file:
    text = file.read()

# tokenize the text into sentences, then tokenize each sentence into words
sentences = nltk.sent_tokenize(text)
words = [nltk.word_tokenize(sentence) for sentence in sentences]

# perform POS tagging to identify verbs and nouns
tagged_words = [nltk.pos_tag(sentence) for sentence in words]
verbs_and_nouns = []
for sentence in tagged_words:
    verbs_and_nouns.extend(
        word
        for word, tag in sentence
        if tag.startswith('NN') or tag.startswith('VB')
    )
# identify collocations
finder = nltk.collocations.BigramAssocMeasures()
bigram_finder = nltk.collocations.BigramCollocationFinder.from_words(verbs_and_nouns)
bigram_finder.apply_freq_filter(3)
collocations = bigram_finder.nbest(finder.pmi, 10)

# identify phrasal verbs
phrasal_verbs = []
for sentence in tagged_words:
    for i in range(len(sentence)-1):
        word1, tag1 = sentence[i]
        word2, tag2 = sentence[i+1]
        if tag1.startswith('VB') and word2 in ['up', 'out', 'off', 'over', 'down', 'on', 'back', 'in', 'away', 'through', 'onto']:
            phrasal_verbs.append(f'{word1} {word2}')

# print the results
print('Collocations: ', collocations)
print('Phrasal Verbs: ', phrasal_verbs)