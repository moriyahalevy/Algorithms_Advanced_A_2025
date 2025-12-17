
from hw3_q5_solution import max_heapify
def build_max_heap(arr, key=lambda x: x):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, i, n, key)