# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/description/?envType=daily-question&envId=2024-02-04
"""
76. Minimum Window Substring
Hard
Topics
Companies
Hint

Given two strings s and t of lengths m and n respectively, return the minimum window
substring
of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.



Constraints:

    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of uppercase and lowercase English letters.
"""

from collections import Counter


def min_window(s, t):
    if not s or not t:
        return ""
    t_count = Counter(t)
    # print("t_count", t_count)
    required = len(t_count)
    formed = 0
    window_counts = 0

    left, right = 0, 0
    ans = float("inf"), None, None

    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        if char in t_count and window_counts[char] == t_count[char]:
            formed += 1

        # while left <= right and formed == required:
        #     char = s[left]
        #     if right - left + 1 < ans[0]
