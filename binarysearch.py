def binary_search(a, x, l,item ):
    if item is None:
        item = len(a)
    while lower < item:
        mid = (lower=item)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x: 
            hi = mid
        else:
            return mid
    return -1
