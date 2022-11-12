class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        try:
            return self.items.pop(0)
        except Exception:
            print("STACK is empty")

    def print_stack(self):
        print(self.items)


s = Stack()
s.push("a")
s.push("b")
s.push("c")
s.print_stack()

s.pop()

s.print_stack()

print(s.is_empty())

s.pop()
s.pop()

s.print_stack()

print(s.is_empty())

s.pop()

print()


def print_methods(object):
    """Prints the method of the pass object"""
    for method in dir(object):
        if method[0] != "_":
            print("Method =>", method)


print("\nNow, this is for me to know the methods of any object\n")
print("For example, 's', in this case:\n")
print_methods(s)
