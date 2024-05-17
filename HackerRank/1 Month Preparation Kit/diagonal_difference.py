def diagonalDifference(arr):
    sizes = [len(a) for a in arr]
    the_size = max(sizes)
    i = 0
    j = -1
    l_to_r_sum = r_to_l_sum = 0
    for a in arr:
        if len(a) == the_size:
            l_to_r_sum += a[i]
            i += 1
            r_to_l_sum += a[j]
            j -= 1
    return abs(l_to_r_sum - r_to_l_sum)
