def sliding_window(arr, k):
    # k => the size of the window
    size = len(arr)
    if k > size:
        return None
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(size - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    return max_sum


"""
size = 6
k = 2
[3,4,6,7,8,2]
"""

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
max_sum = sliding_window(arr, k)
print("Maximum sum of a window of size", k, "in", arr, "is", max_sum)
