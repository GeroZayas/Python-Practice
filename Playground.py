from random import sample, choice

d = {"spam": 2, "eggs": 3, "green stuff": 4}

random_value = sample(list(d.values()), 1)
print("random_value: ", random_value)

random_value = d[choice(list(d.keys()))]
print("random_value: ", random_value)
