# ============= BITWISE OPERATIONS ================


# ============ AND =============

a = 10
b = 6

and_result = a & b

print("a:", bin(a)[2:], "b:", bin(b)[2:])
print("a and b -> ", a, ",", b)

print("And result:", bin(and_result)[2:])
print(and_result)

# ============ OR =============
or_result = a | b

print("Or result", bin(or_result)[2:])
print(or_result)

# ============ XOR =============
xor_result = a ^ b

print("XOR result", bin(xor_result)[2:])
print(xor_result)


# ============ NOT =============
not_result = ~a

print("NOT result", bin(not_result))
print(not_result)


# ============ LEFT SHIFT =============
left_shift = a << 2

print("Left Shift result", bin(left_shift)[2:])
print(left_shift)

# ============ right SHIFT =============
right_shift = a >> 2

print("Right Shift result", bin(right_shift)[2:])
print(right_shift)
