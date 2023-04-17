arr = [3,2,6,5,4,8,7]
print(arr)

arr.sort()
print(arr)

mid = len(arr) // 2; print("mid", mid)


arr[mid], arr[-1] = arr[-1], arr[mid]


st = arr[mid + 1]; print(st)

ed = arr[-1]; print(ed)

while st < ed:
	print(arr)
	st += 1

print(arr)