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

    return Solution,


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
