import argparse
import numpy as np
import os
from rich import print


# ------------------------------ STRUCTS ------------------------------
class Todo:
    __slots__ = "name"

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Todo: {self.name}"


# ------------------------------ ARRAYS ------------------------------


# ------------------------------ PROCEDURES ------------------------------
def add_todo(todo: Todo) -> str:
    with open("todos.txt", "a") as f:
        f.write(todo)
    print("TODO ADDED")


def see_todo() -> np.array:
    with open("todos.txt", "r") as f:
        f.read(todo)


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def especial_print(data: str):
    to_print = f"""
========================================
--- {data}
========================================
    """
    print(to_print)


# ------------------------------ PROCEDURES DISPATCH ------------------------------
commands = {
    "add": add_todo,
    "see": see_todo,
}


# ------------------------------ APP ENTRY POINT ------------------------------
def main():
    parser = argparse.ArgumentParser(description="Todos App")

    sub = parser.add_subparsers(dest="command", required=True)

    add_parser = sub.add_parser("add", help="Adds a task to list of todos")
    add_parser.add_argument("-t", "--task", help="Tasks description")

    add_parser_args = add_parser.parse_args()

    especial_print(add_parser_args)

    see_parser = sub.add_parser("see", help="Remove a tasks from list of todos")

    args = parser.parse_args()

    title = " TODO APP "

    print()
    print("=" * 10, title.center(30, "-"), "=" * 10, end="\n\n")

    if args.command == "add":
        r = add_todo()
        especial_print(r)

    elif args.command == "see":
        especial_print("SEE CALLED")


# ------------------------------ RUN THE APP ------------------------------
if __name__ == "__main__":
    main()

    input()

    clear()  # Clean Term screen when leaving the program
