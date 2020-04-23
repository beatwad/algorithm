import random


def quick_sort(_list, fst, lst):
    """ Performs quick sort algorithm """
    # if first element is bigger than last - return
    if fst >= lst:
        return

    i, j = fst, lst
    # assign random pivot point
    pivot = _list[random.randint(fst, lst)]

    while i <= j:
        # if i-th element less than pivot point - move next
        while _list[i] < pivot:
            i += 1
        # if j-th element more than pivot point - move next
        while _list[j] > pivot:
            j -= 1
        # find i-th element which more than pivot and j-th element which less than pivot
        # and replace them with each other
        if i <= j:
            _list[i], _list[j] = _list[j], _list[i]
            i, j = i + 1, j - 1
    # recursively sort both lists left and right of pivot point
    quick_sort(_list, fst, j)
    quick_sort(_list, i, lst)


a = [17, 27, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0, 4]
quick_sort(a, 0, len(a)-1)
print(a)
