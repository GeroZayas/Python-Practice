import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __(List):
    class Solution:
        def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            ROWS, COLS = len(matrix), len(matrix[0])

            top, bot = 0, ROWS - 1
            while top <= bot:
                row = (top + bot) // 2
                if target > matrix[row][-1]:
                    top = row + 1
                elif target < matrix[row][0]:
                    bot = row - 1
                else:
                    break

            if not (top <= bot):
                return False
            row = (top + bot) // 2
            l, r = 0, COLS - 1
            while l <= r:
                m = (l + r) // 2
                if target > matrix[row][m]:
                    l = m + 1
                elif target < matrix[row][m]:
                    r = m - 1
                else:
                    return True
            return False

    return Solution,


@app.cell
def __(Solution):
    s = Solution()
    return s,


@app.cell
def __():
    matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target = 15
    return matrix, target


@app.cell
def __(matrix, s, target):
    s.searchMatrix(matrix, target)
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
