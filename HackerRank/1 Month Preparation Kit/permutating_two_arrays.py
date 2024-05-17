def twoArrays(k, A, B):
    x = sum(A) / len(A)
    y = sum(B) / len(B)
    return "YES" if x + y >= k and abs(x - y) < k else "NO"
