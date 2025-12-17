def parent(i):
    if i == 0:
        return None  
    return (i - 1) // 2
def left(i):
    return 2 * i + 1
def right(i):
    return 2 * i + 2