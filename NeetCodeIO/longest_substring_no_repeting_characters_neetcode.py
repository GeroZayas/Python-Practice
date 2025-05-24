import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __():
    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            charSet = set()
            l = 0
            res = 0

            for r in range(len(s)):
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
                charSet.add(s[r])
                res = max(res, r - l + 1)
            return res

    return (Solution,)


@app.cell
def __(Solution):
    solution = Solution()
    s = "zxyzxyz"
    s_2 = "xxxx"
    return s, s_2, solution


@app.cell
def __(s, solution):
    print(solution.lengthOfLongestSubstring(s))
    return


@app.cell
def __(s_2, solution):
    print(solution.lengthOfLongestSubstring(s_2))
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
