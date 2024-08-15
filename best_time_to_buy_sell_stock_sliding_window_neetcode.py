import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __(List):
    class Solution:
        def maxProfit(self, prices: List[int]) -> int:
            res = 0
            
            lowest = prices[0]
            for price in prices:
                if price < lowest:
                    lowest = price
                res = max(res, price - lowest)
            return res
    return Solution,


@app.cell
def __(Solution):
    solution = Solution()
    prices = [10,1,5,6,7,1]

    return prices, solution


@app.cell
def __(prices, solution):
    print(solution.maxProfit(prices))
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
