from googlesearch import search

results = search(term="Python news", num_results=10, lang="ca")

results = list(results)

print(results)
