from faker import Faker

faker = Faker()

random_words = []

for x in range(10):
    random_words.append(faker.word())


print("random_words: ", random_words)
