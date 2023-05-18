
def topK_frequent(nums:list, k:int)->list[int]:
	count = {}
	freq = [[] for _ in range(len(nums)+1)]

	for n in nums:
		count[n] = 1 + count.get(n, 0)

	for n, c in count.items():
		freq[c].append(n)
	

	res = []

	for i in range(len(freq) - 1, 0, -1):
		for n in freq[i]:
			res.append(n)
			if len(res) == k:
				return res


nums = [3,3,3,4,4,5,7,7,7,7]; k = 2 # [7,3]

r = topK_frequent(nums, k)
print('r: ', r)