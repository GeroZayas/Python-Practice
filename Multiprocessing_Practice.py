# 100 multiprocessing practice.py
from multiprocessing import Process
import os
import time


def square_nums():
    result = 0
    for i in range(100):
        result += i * i
        time.sleep(0.1)

    return result


print(square_nums())

processes = []
num_processes = os.cpu_count()  # 4

print(num_processes)


# create processes
for _ in range(4):
    p = Process(target=square_nums)
    processes.append(p)


# start
for p in processes:
    p.start()

# join

for p in processes:
    p.join()


print("End Main")
