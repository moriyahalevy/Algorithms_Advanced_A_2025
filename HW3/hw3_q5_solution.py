def max_heapify(arr, i, heap_size, key=lambda x: x):
    left = 2 * i + 1
    right = 2 * i + 2    
    largest = i  
    
    if left < heap_size and key(arr[left]) > key(arr[largest]):
        largest = left
        
    if right < heap_size and key(arr[right]) > key(arr[largest]):
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] 
        max_heapify(arr, largest, heap_size, key)