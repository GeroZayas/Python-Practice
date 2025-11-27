import marimo

__generated_with = "0.14.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import urllib
    return (urllib,)


@app.cell
def _(urllib):
    r = urllib.parse.urlparse(url="https://www.gerozayas.com/")
    return (r,)


@app.cell
def _(r):
    r
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
