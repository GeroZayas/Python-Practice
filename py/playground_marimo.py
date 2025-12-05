import marimo

__generated_with = "0.18.0"
app = marimo.App(width="medium", auto_download=["html", "ipynb"])


@app.cell
def _():
    import fcntl
    return (fcntl,)


@app.cell
def _():
    from rich import inspect
    return (inspect,)


@app.cell
def _(fcntl, inspect):
    inspect(fcntl, methods=True, help=True)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
