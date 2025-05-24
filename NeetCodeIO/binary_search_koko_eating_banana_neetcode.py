import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __():
    import math

    return (math,)


@app.cell
def __(List, math):
    class Solution:
        def minEatingSpeed(self, piles: List[int], h: int) -> int:
            l, r = 1, max(piles)
            res = r

            while l <= r:
                k = (l + r) // 2

                totalTime = 0
                for p in piles:
                    totalTime += math.ceil(float(p) / k)
                if totalTime <= h:
                    res = k
                    r = k - 1
                else:
                    l = k + 1
            return res

    return (Solution,)


@app.cell
def __(Solution):
    s = Solution()
    return (s,)


@app.cell
def __():
    piles = [25, 10, 23, 4]
    h = 4
    return h, piles


@app.cell
def __(h, piles, s):
    s.minEatingSpeed(piles, h)
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
