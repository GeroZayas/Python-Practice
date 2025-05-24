import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __(List):
    class Solution:
        def search(self, nums: List[int], target: int) -> int:
            l, r = 0, len(nums) - 1

            while l <= r:
                m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return m
            return -1

    return (Solution,)


@app.cell
def __(Solution):
    s = Solution()
    return (s,)


@app.cell
def __():
    nums = [-1, 0, 2, 4, 6, 8]
    target = 4
    return nums, target


@app.cell
def __(nums, s, target):
    s.search(nums, target)
    return


@app.cell
def __(s):
    nums2 = [-1, 0, 2, 4, 6, 8]
    target2 = 3
    s.search(nums2, target2)
    return nums2, target2


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
