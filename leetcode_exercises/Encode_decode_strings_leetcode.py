
def encode(strs:list[str]) -> str:
	return ''.join(f'{len(s)}#{s}' for s in strs)

x = encode(['gero', 'zayas'])

print(x)

def decode(string:str):
	res = []
	i = 0
	while i < len(string):
		j = i
		while string[j] != '#':
			j += 1
		length = int(string[i:j])
		word = string[j+1: j + length + 1]
		res.append(word)
		i += j + length + 1

	return res


print(decode(x))