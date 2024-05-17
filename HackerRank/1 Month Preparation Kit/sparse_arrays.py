def matchingStrings(strings, queries):
    fin_count = []
    for q in queries:
        c = strings.count(q)
        fin_count.append(c)
    return fin_count
