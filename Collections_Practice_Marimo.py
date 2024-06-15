import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __():
    import collections
    return collections,


@app.cell
def __():
    from rich import inspect
    return inspect,


@app.cell
def __(collections, inspect):
    inspect(collections, methods=True)
    return


@app.cell
def __():
    dict_one = {"name": "Gero", "age": 32}
    return dict_one,


@app.cell
def __():
    dict_two = {"profession": "programmer", "job": "BBVA"}
    return dict_two,


@app.cell
def __(collections, dict_one, dict_two):
    together = collections.ChainMap(dict_one, dict_two)
    return together,


@app.cell
def __(together):
    together
    return


@app.cell
def __(together):
    for k, v in together.items():
        print(k, "->", v)
    return k, v


@app.cell
def __(collections, together):
    counter = collections.Counter(together)
    return counter,


@app.cell
def __(counter):
    counter.values()
    return


@app.cell
def __(collections, inspect):
    inspect(collections.defaultdict, methods=True, docs=True)
    return


@app.cell
def __(collections):
    new_def_dict = collections.defaultdict(list)
    return new_def_dict,


@app.cell
def __(new_def_dict):
    new_def_dict
    return


@app.cell
def __(new_def_dict):
    new_def_dict["names"]
    return


@app.cell
def __(new_def_dict):
    type(new_def_dict["names"])
    return


@app.cell
def __(new_def_dict):
    new_def_dict["names"].append(34)
    return


@app.cell
def __(new_def_dict):
    new_def_dict
    return


@app.cell
def __(new_def_dict):
    type(new_def_dict["names"][0])
    return


@app.cell
def __(collections):
    new_deque = collections.deque()
    return new_deque,


@app.cell
def __(new_deque):
    new_deque
    return


@app.cell
def __(new_deque):
    new_deque.append(34)
    return


@app.cell
def __(new_deque):
    new_deque.append(23)
    return


@app.cell
def __(new_deque):
    new_deque
    return


@app.cell
def __(new_deque):
    new_deque.appendleft(88)
    return


@app.cell
def __(new_deque):
    new_deque
    return


@app.cell
def __(new_deque):
    new_deque.rotate(1)

    return


@app.cell
def __(new_deque):
    new_deque
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
