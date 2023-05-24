
'''
Input: s = "A man, a plan, a canal: Panama"

Output: true

Explanation: "amanaplanacanalpanama" is a palindrome.
'''

# SOLUTION 1
'''
Creates extra memory by creating a new string and also a reversed one at the end of the function
'''

def isPalindrome1(s: str) -> bool:
	new_string = ''
	for c in s:
		if c.isalnum():
			new_string += c.lower()
	return new_string == new_string[::-1]

print("Solution 1: ->  ", isPalindrome1(s = "A man, a plan, a canal: Panama"))


# SOLUTION 2
'''
- We create a helper function for this one, to avoid using the bultin funct
of isalnum(), we write our own
- This solution is constant extra memory, we use POINTERS in this case (more memory efficient, not using extra memory to create a new string like in solution 1) 
'''


# Helper function
def isalphanumeric(c)->bool:
	if (ord('A') <= ord(c) <= ord('Z') or
		ord('a') <= ord(c) <= ord('z') or
		ord('0') <= ord(c) <= ord('9')):
		return True
	return False



def isPalindrome2(s: str) -> bool:
	# left pointer -> l , right pointer -> r
	l = 0
	r = len(s) - 1

	while l < r:
		while l < r and not isalphanumeric(s[l]):
			l += 1

		while r > l and not isalphanumeric(s[r]):
			r -= 1

		if s[l].lower() != s[r].lower():
			return False
		l, r = l + 1, r - 1

	return True

print("Solution 2: ->  ", isPalindrome2(s = "A man, a plan, a canal: Panama"))
		