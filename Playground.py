def sliding_window(arr, k):
    # k => the size of the window
    size = len(arr)
    if k > size:
        return None
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(size-k):
    
    
"""
size = 6
k = 2
[3,4,6,7,8,2]
"""