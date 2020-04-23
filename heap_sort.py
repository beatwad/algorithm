def max_heapify(_list, heap_len, i):
    """ Creates heap from _listay"""
    largest = i
    left = 2*i+1
    right = 2*i+2
    # Check if left element that more than root exists
    if left < heap_len and _list[left] > _list[i]:
        largest = left
    # Check if right element that more than root exists
    if right < heap_len and _list[right] > _list[largest]:
        largest = right
    # Replace root if necessary
    if largest != i:
        _list[i], _list[largest] = _list[largest], _list[i]
        # heapify the root
        max_heapify(_list, heap_len, largest)


def build_max_head(_list):
    """ Builds heap from _listay """
    length = len(_list)
    for i in range(length, -1, -1):
        max_heapify(_list, len(_list), i)


def heap_sort(_list):
    """ Sorts heap """
    build_max_head(_list)
    for i in range(len(_list)-1, 0, -1):
        _list[0], _list[i] = _list[i], _list[0]
        max_heapify(_list, i, 0)


a = [17, 27, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0, 4]
heap_sort(a)
print(a)
