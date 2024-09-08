import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __(List):
    class Solution:
        def generateParenthesis(self, n: int) -> List[str]:
            stack = []
            res = []

            def backtrack(openN, closedN):
                if openN == closedN == n:
                    res.append("".join(stack))
                    return

                if openN < n:
                    stack.append("(")
                    backtrack(openN + 1, closedN)
                    stack.pop()
                if closedN < openN:
                    stack.append(")")
                    backtrack(openN, closedN + 1)
                    stack.pop()

            backtrack(0, 0)
            return res

    return Solution,


@app.cell
def __(Solution):
    solution = Solution()
    return solution,


@app.cell
def __():
    n = 3
    return n,


@app.cell
def __(n, solution):
    solution.generateParenthesis(n)
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
