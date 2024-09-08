import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __():
    class TimeMap:

        def __init__(self):
            self.keyStore = {}  # key : list of [val, timestamp]

        def set(self, key: str, value: str, timestamp: int) -> None:
            if key not in self.keyStore:
                self.keyStore[key] = []
            self.keyStore[key].append([value, timestamp])

        def get(self, key: str, timestamp: int) -> str:
            res, values = "", self.keyStore.get(key, [])
            l, r = 0, len(values) - 1
            while l <= r:
                m = (l + r) // 2
                if values[m][1] <= timestamp:
                    res = values[m][0]
                    l = m + 1
                else:
                    r = m - 1
            return res

    return TimeMap,


@app.cell
def __(TimeMap):
    timemap = TimeMap()
    timemap.set("alice", "happy", 1)
    return timemap,


@app.cell
def __(timemap):
    timemap.get("alice", 1)
    return


@app.cell
def __(timemap):
    timemap.get("alice", 2)
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
