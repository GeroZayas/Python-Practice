
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

print(isPalindrome1(s = "A man, a plan, a canal: Panama"))


# SOLUTION 2

def isPalindrome2(s: str) -> bool:
	...