

from typing import List
from collections import defaultdict, Counter

def groupAnagrams(strs:List[str])->List[List[str]]:
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)
    return res

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs=strs))

