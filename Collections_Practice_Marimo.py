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
    people = collections.namedtuple("People", ["name", "age"])
    return people,


@app.cell
def __(people):
    gero = people("gero", 32)
    return gero,


@app.cell
def __(gero):
    gero
    return


@app.cell
def __(gero):
    gero.age
    return


@app.cell
def __(gero):
    gero.name
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
