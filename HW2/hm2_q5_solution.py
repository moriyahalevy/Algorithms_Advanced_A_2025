def dual_pivot_partition(a, key=lambda x: x):
    start = 0
    end = len(a) - 1
    if key(a[start]) > key(a[end]):
        a[start], a[end] = a[end], a[start]
    
    pivot1_value = key(a[start])
    pivot2_value = key(a[end])
    L = start + 1 
    G = end - 1
    K = start + 1
    while K <= G:
        k_val = key(a[K])

        if k_val < pivot1_value:

            a[K], a[L] = a[L], a[K]
            L += 1
            K += 1
            
        elif k_val >= pivot2_value:

            while K <= G and key(a[G]) >= pivot2_value:
                G -= 1
            
            if k_val > key(a[G]):

                a[K], a[G] = a[G], a[K]


            if key(a[K]) < pivot1_value:
                a[K], a[L] = a[L], a[K]
                L += 1
            
            G -= 1
            K += 1 
            
        else:

            K += 1


    L -= 1
    a[start], a[L] = a[L], a[start]

    G += 1
    a[end], a[G] = a[G], a[end]
 
    return L, G