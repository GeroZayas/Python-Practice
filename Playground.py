def has_zero_sum_list(nums):
    s = {0} # we create a set and we add zero to it
    total = 0
    for i in nums:
        print(f"Total {total} + {i} (i)")
        total += i
        print(f"Set {s}", f"Total {total}")
        if total in s:
            return True
        s.add(total)
    
    return False

if __name__ == '__main__':
 
    nums = [0, 4, -6, 3, -1, 4, 2, 7]
 
    if has_zero_sum_list(nums):
        print('Sublist exists')
    else:
        print('Sublist does not exist')
    