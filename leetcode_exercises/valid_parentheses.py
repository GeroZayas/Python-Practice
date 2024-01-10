def is_valid(s: str) -> bool:
    MAP = {"}": "{", "]": "[", ")": "("}
    stack = []
    for c in s:
        if c not in MAP:
            stack.append(c)
            continue
        if not stack or stack[-1] != MAP[c]:
            return False
        stack.pop()
    return not stack


s = "([])"
print(is_valid(s))  # true

s2 = "({[])}"
print(is_valid(s2))  # false
