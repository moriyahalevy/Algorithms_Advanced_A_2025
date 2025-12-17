def _parent_index(i):
    return (i - 1) // 2

def is_max_heap(arr, i=0, key=lambda x: x):
    n = len(arr)
    if n <= i:
        return True
    
    for current_index in range(i + 1, n):
        parent_index = _parent_index(current_index)
        
        if parent_index >= i:
            parent_key = key(arr[parent_index])
            current_key = key(arr[current_index])

            if parent_key < current_key:
                return False  
                
    return True