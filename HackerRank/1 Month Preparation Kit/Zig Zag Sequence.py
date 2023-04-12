def findZigZagSequence(a, n):
    a.sort()
    
    print(a)
    
    mid = int((n + 1)/2) - 1
    
    print("mid", mid)

    print("a[mid]", a[mid])
    
    a[mid], a[n-1] = a[n-1], a[mid]

    print(a)

    st = mid + 1
    print('st', st, 'a[st]', a[st]); 

    ed = st + 1
    print('ed',ed, 'a[ed]', a[ed])
    while(a[st] <= a[ed]):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

a = [1,2,3,4,5,6,7]

n = 7

r = findZigZagSequence(a,n)

expected = [1,2,3,7,6,5,4]

print('This is r', r)

print(r == expected)