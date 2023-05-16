from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
        dic = {}

        for s in strs:
            word_list = [0] * 26
            for c in s:
                dic[word_list] = 1 + word_list.get(c, 0)
        print(dic)
