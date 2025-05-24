import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __():
    class Solution:
        def characterReplacement(self, s: str, k: int) -> int:
            count = {}

            l = 0
            maxf = 0
            for r in range(len(s)):
                count[s[r]] = 1 + count.get(s[r], 0)
                maxf = max(maxf, count[s[r]])

                if (r - l + 1) - maxf > k:
                    count[s[l]] -= 1
                    l += 1

            return r - l + 1

    return (Solution,)


@app.cell
def __(Solution):
    solution = Solution()
    return (solution,)


@app.cell
def __():
    s = "XYYX"
    k = 2
    return k, s


@app.cell
def __(k, s, solution):
    print(solution.characterReplacement(s, k))
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
