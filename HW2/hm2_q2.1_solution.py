
def merge(a, b, key=lambda x: x):  
    merged_list = []
    i = j = 0  

    while i < len(a) and j < len(b):
        key_a = key(a[i])
        key_b = key(b[j])

        if key_a <= key_b:
            merged_list.append(a[i])
            i += 1
        else:
            merged_list.append(b[j])
            j += 1

    merged_list.extend(a[i:])
    merged_list.extend(b[j:])
    
    return merged_list

