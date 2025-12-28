# פונקציית ה-Partition (לפי לומטו)
def partition(arr, left, right, key):
    pivot_value = arr[right]
    i = left
    for j in range(left, right):
        if key(arr[j]) <= key(pivot_value):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

def quick_kth(arr, left, right, k, key=lambda x: x):
    if left == right:
        return arr[left]
    
    pivot_index = partition(arr, left, right, key)
    
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quick_kth(arr, left, pivot_index - 1, k, key)
    else:
        return quick_kth(arr, pivot_index + 1, right, k, key)