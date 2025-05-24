import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __():
    # 	Find Minimum In Rotated Sorted Array
    return


@app.cell
def __(List):
    class Solution:
        def findMin(self, nums: List[int]) -> int:
            start, end = 0, len(nums) - 1
            curr_min = float("inf")

            while start < end:
                mid = start + (end - start) // 2
                curr_min = min(curr_min, nums[mid])

                # right has the min
                if nums[mid] > nums[end]:
                    start = mid + 1

                # left has the  min
                else:
                    end = mid - 1

            return min(curr_min, nums[start])

    return (Solution,)


@app.cell
def __(Solution):
    s = Solution()
    return (s,)


@app.cell
def __(s):
    s.findMin(nums=[3, 4, 5, 6, 1, 2])
    return


@app.cell
def __(s):
    s.findMin(nums=[4, 5, 6, 7])
    return


@app.cell
def __(s):
    s.findMin(nums=[2, 34, 1, 56])
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
