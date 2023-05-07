from typing import List
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
   

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs=strs))

strs = ['a', 'b', 'b']

print(groupAnagrams(strs=strs))

strs = ['']

print(groupAnagrams(strs=strs))