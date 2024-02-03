from collections import Counter

string = "This is my string and my name is Gero"

counter = Counter(string)

print(counter.most_common()[3])

print(dir(Counter))

print(sorted(counter.items(), key=lambda x: x[1]))
