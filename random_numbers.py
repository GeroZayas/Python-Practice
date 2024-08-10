import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __():
    import random
    return random,


@app.cell
def __(random):
    number = random.randint(0, 9)
    return number,


@app.cell
def __(number):
    number
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
