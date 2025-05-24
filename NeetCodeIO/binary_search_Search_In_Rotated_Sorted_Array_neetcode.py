import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __(List):
    class Solution:
        def search(self, nums: List[int], target: int) -> int:
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = (l + r) // 2
                if target == nums[mid]:
                    return mid

                if nums[l] <= nums[mid]:
                    if target > nums[mid] or target < nums[l]:
                        l = mid + 1
                    else:
                        r = mid - 1

                else:
                    if target < nums[mid] or target > nums[r]:
                        r = mid - 1
                    else:
                        l = mid + 1
            return -1

    return (Solution,)


@app.cell
def __(Solution):
    s = Solution()
    return (s,)


@app.cell
def __(s):
    s.search(nums=[3, 4, 5, 6, 1, 2], target=1)
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
