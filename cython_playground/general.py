from multiprocessing import Pool
import multiprocessing
from time import perf_counter
import sys
import powerful

sys.set_int_max_str_digits(32000)

cube = powerful.cube

def main(processes: int = 2):
    print(f"{multiprocessing.cpu_count()= }")

    # breakpoint()
    
    my_iterable = range(1, 8000)


    start = perf_counter()

    results = 0

    with Pool(processes=processes) as pool:
        results = sum(pool.map(cube, my_iterable))

    print(results)

    end = perf_counter()

    print("==" * 50)
    print("TIME", end - start)
    print("==" * 50)

if __name__ == "__main__":
    main(2)