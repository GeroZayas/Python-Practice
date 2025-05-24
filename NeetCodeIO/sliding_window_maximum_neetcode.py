import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __(List, deque):
    class Solution:
        def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            output = []
            q = deque()  # index
            l = r = 0

            while r < len(nums):
                while q and nums[q[-1]] < nums[r]:
                    q.pop()
                q.append(r)

                if l > q[0]:
                    q.popleft()

                if (r + 1) >= k:
                    output.append(nums[q[0]])
                    l += 1
                r += 1

            return output

    return (Solution,)


@app.cell
def __():
    from collections import deque

    nums = [1, 2, 1, 0, 4, 2, 6]
    k = 3
    return deque, k, nums


@app.cell
def __(Solution):
    solution = Solution()
    return (solution,)


@app.cell
def __(k, nums, solution):
    solution.maxSlidingWindow(nums, k)
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
