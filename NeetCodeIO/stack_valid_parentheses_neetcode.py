import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __():
    class Solution:
        def isValid(self, s: str) -> bool:
            Map = {")": "(", "]": "[", "}": "{"}
            stack = []

            for c in s:
                if c not in Map:
                    stack.append(c)
                    continue
                if not stack or stack[-1] != Map[c]:
                    return False
                stack.pop()

            return not stack

    return (Solution,)


@app.cell
def __(Solution):
    solution = Solution()
    return (solution,)


@app.cell
def __():
    s = "([{}])"
    return (s,)


@app.cell
def __(s, solution):
    solution.isValid(s)
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
