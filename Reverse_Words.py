def reverse_words(sentence:str)->str:
    """
    A function that reverses the input string.
    """
    lis = sentence.split()
    res = []
    for word in lis:
        res.append(word[::-1])
    print(" ".join(res))

reverse_words("Hello Gero")

