from hw3_q6_solution import build_max_heap
from hw3_q5_solution import max_heapify
def heap_sort(arr, key=lambda x: x):
    n = len(arr)

    build_max_heap(arr, key)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, 0, i, key)