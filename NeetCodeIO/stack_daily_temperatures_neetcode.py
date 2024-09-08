import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __(List):
    class Solution:
        def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            res = [0] * len(temperatures)
            stack = []  # pair: [temp, index]

            for i, t in enumerate(temperatures):
                while stack and t > stack[-1][0]:
                    stackT, stackInd = stack.pop()
                    res[stackInd] = i - stackInd
                stack.append((t, i))
            return res

    return Solution,


@app.cell
def __(Solution):
    solution = Solution()
    return solution,


@app.cell
def __():
    temperatures = [30,38,30,36,35,40,28]
    return temperatures,


@app.cell
def __(solution, temperatures):
    solution.dailyTemperatures(temperatures)
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
