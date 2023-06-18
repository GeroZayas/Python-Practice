def reverse_words(sentence:str)->str:
    lis = sentence.split()
    res = []
    for word in lis:
        res.append(word[::-1])
    print(" ".join(res))

reverse_words("Hello Gero")
