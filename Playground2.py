from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]: # type: ignore
    res = defaultdict(list)
    the_words = strs
    for word in the_words:
        count = [0] * 26
        for character in word:
            count[ord(character) - ord('a')] += 1
        res[tuple(count)].append(word)
    return res.values() # type: ignore

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs=strs))
