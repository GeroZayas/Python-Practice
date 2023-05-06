def two_sum(arr:list, target:int):
    '''
    Returns the indeces of two values in the arr that add up to target
    '''
    size = len(arr)
    
    for i in range(size):
        for j in range(i+1, size):
            if arr[i] + arr[j] == target:
                return [i,j]
    return None

numbers = [4,5,3,2,9,7]

target = 13

r = two_sum(numbers, target)
print('r: ', r)