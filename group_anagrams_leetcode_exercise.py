from typing import List
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    ans = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[count].append(s)

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs=strs))

strs = ['a', 'b', 'b']

print(groupAnagrams(strs=strs))

strs = ['']

print(groupAnagrams(strs=strs))