import fire

def add(x, y):
    return f"{x} + {y} = {x+y}"


def substract(x, y):
    return f"{x} - {y} = {x-y}"

if __name__ == "__main__":
    fire.Fire()
