from googlesearch import search

results = search(term="Cuba news", num_results=10, lang="ca")

results = list(results)

print(results)

