class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


# -------------------------------
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

    # easier solution
    # return True if sorted(s) == sorted(t) else False


# -------------------------------
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans


# -------------------------------
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr


# -------------------------------
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


# -------------------------------
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        one shortcut
        """
        #   return len(s.split()[-1])
        c = 0
        for i in s[::-1]:
            if i == " ":
                if c >= 1:
                    return c
            else:
                c += 1
        return c


# -------------------------------


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


# -------------------------------
class Solution:
    for i in range(len(strs[0])):
        for s in strs:
            if i >= len(s) or s[i] != strs[0][i]:
                return strs[0][:i]
    return strs[0]


# -------------------------------


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()


# -------------------------------
class Solution:
    def generate(self, rowIndex) -> List[List[int]]:
        if rowIndex == 0:
            return [[1]]
        else:
            return self.getAllRow(rowIndex - 1)

    def getAllRow(self, rowIndex):
        if rowIndex == 0:
            return [[1]]
        ListPrec = self.getAllRow(rowIndex - 1)
        Len = len(ListPrec[-1])
        ListPrec.append([1])
        for i in range(0, Len - 1):
            ListPrec[-1].append(ListPrec[-2][i] + ListPrec[-2][i + 1])
        ListPrec[-1].append(1)
        return ListPrec


# -------------------------------
