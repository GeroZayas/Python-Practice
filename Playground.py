
def valid_palindrome(string:str)->bool:
	def is_al_num(c)->bool:
		if (ord('A') <= ord(c) <= ord('Z') or
			ord('a') <= ord(c) <= ord('z') or
			ord('0') <= ord(c) <= ord('9')):
			return True
		return False

	l, r = 0, len(string) - 1

	while l < r:
		while l < r and not is_al_num(string[l]):
			l += 1
		while r > l and not is_al_num(string[r]):
			r -= 1

		if string[l].lower() != string[r].lower():
			return False

		l, r = l + 1, r - 1

	return True

res = valid_palindrome(string = 'My name is Gero')
print(res) # False

res = valid_palindrome(string = "A man, a plan, a canal: Panama")
print(res) # True