class Queue:
    def __init__(self):x
        self.items = []

    def print_queue(self):
        return self.items

    def esta_vacia(self):
        return "Esta vacia!" if self.items == [] else "Tiene elementos!"

    def enqueue(self, elemento):
        self.items.insert(0, elemento)

    def dequeue(self):
        return self.items.pop()


my_first_queue = Queue()

print(my_first_queue.print_queue())
print(my_first_queue.esta_vacia())


my_first_queue.enqueue("Gero")

print(my_first_queue.print_queue())
print(my_first_queue.esta_vacia())

my_first_queue.enqueue("Mareta")
my_first_queue.enqueue("Elisa")
my_first_queue.enqueue("Enrique")
my_first_queue.enqueue("Zayitas")


print(my_first_queue.print_queue())
print(my_first_queue.esta_vacia())

se_va_ahora = my_first_queue.dequeue()

print("Se va:", se_va_ahora)
