def maxArea(height: list[int]) -> int:
    res = 0
    # this is a two pointer solution
    # we have left 'l' all the way to the left
    # all the way to the right -> right 'r'
    l, r = 0, len(height) - 1
    # condition, left index cannot surpass nor equal the right one
    while l < r:
        # we calculate the area
        # the right index - the left index to find the x value
        # then the lower [shorter] value for the height to have the y value
        # it has to be the shorter because if not the water would spill out
        # the problem is about finding the largest container for water
        area = (r - l) * min(height[l], height[r])
        # then res will take the value of area if the latter is higher
        res = max(area, res)
        # then we have to move our indexes accordingly
        if height[l] < height[r]:
            # we keep the higher wall, the higher y so we can find the max area
            l += 1
        else:
            # for the other two cases, l higher, or both equal, we can do the same
            r -= 1
    return res


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]  # 49

print("---------------------------")
print(maxArea(height))
