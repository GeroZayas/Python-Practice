import uvicorn
from typing import Annotated, Union, Literal, List
from fastapi import FastAPI, Query


app = FastAPI()

my_data = {"name": "Gero", "age": 30, "city": "New York", "country": "USA"}

options: List = ["mult", "div", "add", "sub", "expo", "crazy_div", "something"]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/data")
def read_data():
    return my_data


@app.get("/data/{key}")
def read_data_key(key: Literal["age", "city", "name", "country"]):
    return {key: my_data.get(key, "Not found")}


@app.get("/calc/{operation}")
def read_number(
    num_a: Annotated[Union[int | float], Query()],
    num_b: Annotated[Union[int | float], Query()],
    operation: Literal[*options],
):
    res = ""
    match operation:
        case "mult":
            res = num_a * num_b
        case "div":
            res = num_a / num_b
        case "add":
            res = num_a + num_b
        case "sub":
            res = num_a - num_b
        case _:
            res = "NOT CONTEMPLATED"

    return {f"{num_a} {operation} {num_b}": res}


@app.get("/health")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
