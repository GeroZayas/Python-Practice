import typer

app = typer.Typer()


@app.command()
def hello(name: str):
    print("Hello", name)


@app.command()
def goodbye(
    name: str,
    formal: bool = False,
):
    if formal:
        print(f"Good bye MR. {name}. Have a good day")
    else:
        print("Good bye motherlover")
        
if __name__ == "__main__":
    app()
