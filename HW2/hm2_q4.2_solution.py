def hoare_partition(a, key):
    start = 0
    end = len(a) - 1
    pivot_value = key(a[start])
    
    i = start 
    j = end

    while True:
        i += 1
        while i <= end and key(a[i]) <= pivot_value:
            i += 1

        while key(a[j]) > pivot_value:
            j -= 1
        
        if i >= j:
            break

        a[i], a[j] = a[j], a[i]

    a[start], a[j] = a[j], a[start]

    return j