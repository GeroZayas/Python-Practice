def isPalindrome(string: str) -> bool:
    def isalphanum(c) -> bool:
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )

    # we use two pointer l, r
    l = 0
    r = len(string) - 1

    while l < r:
        while l < r and not isalphanum(string[l]):
            l += 1
        while r > l and not isalphanum(string[r]):
            r -= 1
        if string[l].lower() != string[r].lower():
            return False
        l, r = l + 1, r - 1
    return True


print("Solution 2: ->  ", isPalindrome(string="A man, a plan, a canal: Panama"))
