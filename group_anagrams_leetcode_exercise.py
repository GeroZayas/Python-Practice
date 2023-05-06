import typing, collections

def groupAnagrams(strs: typing.List[str]) -> typing.List[typing.List[str]]:
    """
    The function takes a list of strings and groups them into lists of anagrams using a dictionary with
    character count tuples as keys.
    
    :param strs: A list of strings that we want to group into anagrams
    :type strs: typing.List[str]
    :return: a list of lists of strings, where each inner list contains a group of anagrams.
    """
    ans = collections.defaultdict(list)

    for s in strs:
        count = [0] * 26
        print("-" * 60) ####################
        
        for c in s:
            count[ord(c) - ord("a")] += 1
            print('count: ', count)
            print("-" * 60) ####################
            
        ans[tuple(count)].append(s)
        print('ans: ', ans)
        print("-" * 60) ####################
        
    return ans.values()


strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs=strs))