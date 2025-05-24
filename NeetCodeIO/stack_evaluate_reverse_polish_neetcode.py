import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __(List):
    class Solution:
        def evalRPN(self, tokens: List[str]) -> int:
            stack = []
            for c in tokens:
                if c == "+":
                    stack.append(stack.pop() + stack.pop())
                elif c == "-":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                elif c == "*":
                    stack.append(stack.pop() * stack.pop())
                elif c == "/":
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(float(b) / a))
                else:
                    stack.append(int(c))
            return stack[0]

    return (Solution,)


@app.cell
def __(Solution):
    solution = Solution()
    return (solution,)


@app.cell
def __():
    tokens = ["1", "2", "+", "3", "*", "4", "-"]
    return (tokens,)


@app.cell
def __(solution, tokens):
    solution.evalRPN(tokens)
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
