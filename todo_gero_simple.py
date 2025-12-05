import argparse
import os
from rich import print

"""
GO HERE: https://chatgpt.com/c/68da266d-7384-8326-90da-755c824ab7fc

"""


FILEPATH = "todos.txt"


# ------------------------------ FILE I/O ------------------------------
def load_todos(filepath=FILEPATH) -> list[str]:
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as f:
        return [line.strip() for line in f]


def save_todos(todos: list[str], filepath=FILEPATH) -> None:
    with open(filepath, "w") as f:
        f.write("\n".join(todos) + "\n" if todos else "")


# ------------------------------ CORE LOGIC ------------------------------
def add_todo(task: str):
    """
    Adds todo : Todo to the todos.txt file
    """
    todos = load_todos()
    todos.append(task)
    save_todos(todos)
    print("[green]TODO ADDED[/green]")


def see_todo():
    """
    Shows a list of all todos in order from the todos.txt file
    """
    todos = load_todos()
    if not todos:
        print("[red]--- No todos found! EMPTY LIST ---[/red]")
        return
    print("===== ID ===== TASK =====")
    for idx, task in enumerate(todos, start=1):
        print(f"[cyan]{idx}[/cyan] --- {task}")


def clear_todos():
    save_todos([])
    return "[yellow]List of todos cleared![/yellow]"


def delete_todo(index: int):
    todos = load_todos()
    index -= 1
    if 0 <= index < len(todos):
        del todos[index]
        save_todos(todos)
        print(f"[green]Deleted todo #{index + 1}[/green]")
    else:
        print("[red]Invalid ID[/red]")


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


# ------------------------------ APP ENTRY POINT ------------------------------
def main():
    parser = argparse.ArgumentParser(description="Todos App")

    parser.add_argument("-a", "--add", type=str, help="Add a todo")
    parser.add_argument("--see", action="store_true", help="See the list of todos")
    parser.add_argument(
        "--clear-todos", action="store_true", help="Clear (empty) the list of todos"
    )
    parser.add_argument("--delete", type=int, help="Delete a todo base on ID number")

    args = parser.parse_args()

    if args.add:
        add_todo(args.add)

    elif args.see:
        see_todo()

    elif args.clear_todos:
        print(clear_todos())

    elif args.delete:
        delete_todo(int(args.delete))

    else:
        print("something else called")


# ------------------------------ RUN THE APP ------------------------------
if __name__ == "__main__":
    main()

    input()

    clear()  # Clean Term screen when leaving the program
