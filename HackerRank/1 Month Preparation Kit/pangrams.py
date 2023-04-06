def pangrams(s):
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz ')
    print(alphabet_set)
    new_s = s.strip()
    s_set = set(new_s.lower())
    print(s_set)
    return 'pangram' if sorted(alphabet_set) == sorted(s_set) else 'not pangram'