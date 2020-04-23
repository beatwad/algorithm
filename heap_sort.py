def max_heapify(A, heap_len, i):
    """ Creates heap from array"""
    largest = i
    left = 2*i+1
    right = 2*i+2
    # Check if left element that more than root exists
    if left < heap_len and A[left] > A[i]:
        largest = left
    # Check if right element that more than root exists
    if right < heap_len and A[right] > A[largest]:
        largest = right
    # Replace root if necessary
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        # heapify the root
        max_heapify(A, heap_len, largest)


def build_max_head(A):
    """ Builds heap from array """
    length = len(A)
    for i in range(length, -1, -1):
        max_heapify(A, len(A), i)


def heap_sort(A):
    """ Sorts heap """
    build_max_head(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A, i, 0)


A = [17, 27, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0, 4]
heap_sort(A)
print(A)
