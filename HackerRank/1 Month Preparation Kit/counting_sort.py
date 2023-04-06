def countingSort(arr):
    fin_arr = []
    for i in range(100):
        fin_arr.insert(i, arr.count(i))
    return fin_arr