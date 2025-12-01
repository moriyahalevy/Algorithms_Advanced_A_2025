def lomuto_partition(a, key):
    start = 0
    end = len(a) - 1
    pivot_value = key(a[end])
    i = start - 1 

    for j in range(start, end):
        if key(a[j]) <= pivot_value:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[end] = a[end], a[i + 1]
    
    return i + 1