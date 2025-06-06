import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __(List):
    class Solution:
        def largestRectangleArea(self, heights: List[int]) -> int:
            maxArea = 0
            stack = []  # pair: (index, height)

            for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h:
                    index, height = stack.pop()
                    maxArea = max(maxArea, height * (i - index))
                    start = index
                stack.append((start, h))

            for i, h in stack:
                maxArea = max(maxArea, h * (len(heights) - i))
            return maxArea

    return (Solution,)


@app.cell
def __(Solution):
    s = Solution()
    return (s,)


@app.cell
def __(s):
    s.largestRectangleArea(heights=[7, 1, 7, 2, 2, 4])
    return


@app.cell
def __(s):
    s.largestRectangleArea(heights=[1, 3, 7])
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
