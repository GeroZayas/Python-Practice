import marimo

__generated_with = "0.18.0"
app = marimo.App(width="medium", auto_download=["html", "ipynb"])


@app.cell
def _():
    import compileall
    from rich import inspect
    return compileall, inspect


@app.cell
def _(inspect):
    def show(module):
        return inspect(module, methods=True, help=True)
    return (show,)


@app.cell
def _(compileall, show):
    show(compileall.filecmp)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
