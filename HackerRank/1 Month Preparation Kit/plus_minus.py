def plusMinus(arr):
    size = len(arr)
    positive = negative = zeros = 0
    for elem in arr:
        if elem > 0:
            positive += 1
        elif elem < 0:
            negative += 1
        else:
            zeros += 1
    pos_ratio, neg_ratio, zero_ratio = positive / size, negative / size, zeros / size
    print(f"{pos_ratio:.6f}")
    print(f"{neg_ratio:.6f}")
    print(f"{zero_ratio:.6f}")
