def isPalindrome(string: str) -> bool:
    def isalphanum(c: str) -> bool:
        if (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        ):
            return True
        return False
    
    

print(isPalindrome("4"))


# print("Solution 2: ->  ", isPalindrome(s = "A man, a plan, a canal: Panama"))
