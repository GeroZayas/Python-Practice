import marimo

__generated_with = "0.14.13"
app = marimo.App(width="medium")


@app.cell
def _():
    from sys import getsizeof
    import numpy as np
    from collections import namedtuple
    return (np,)


@app.cell
def _(np):
    id(np)
    return


@app.cell
def _():
    name = "Gero"
    return (name,)


@app.cell
def _(name):
    id(name)
    return


@app.cell
def _():
    nombre = "Gero"
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
