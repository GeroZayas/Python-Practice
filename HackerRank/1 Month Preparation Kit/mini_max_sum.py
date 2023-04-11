def miniMaxSum(arr):
    min_num = min(arr)
    max_num = max(arr)
    min_sum = sum(arr) - max_num
    max_sum = sum(arr) - min_num
    print(min_sum, max_sum)