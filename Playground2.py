from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]: # type: ignore
        dic = defaultdict(list)

        for s in strs:
            word_list = [0] * 26
            for c in s:
                dic[word_list] = 1 + 
        print(dic)
        
        
strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs=strs))
