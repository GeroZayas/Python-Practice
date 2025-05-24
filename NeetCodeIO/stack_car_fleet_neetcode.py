import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __(List):
    class Solution:
        def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            pair = [(p, s) for p, s in zip(position, speed)]
            pair.sort(reverse=True)
            stack = []
            for p, s in pair:  # Reverse Sorted Order
                stack.append((target - p) / s)
                if len(stack) >= 2 and stack[-1] <= stack[-2]:
                    stack.pop()
            return len(stack)

    return (Solution,)


@app.cell
def __(Solution):
    solution = Solution()
    target = 10
    position = [1, 4]
    speed = [3, 2]
    return position, solution, speed, target


@app.cell
def __(position, solution, speed, target):
    solution.carFleet(target, position, speed)
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
