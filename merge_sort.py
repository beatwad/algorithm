def merge(_list, begin, middle, end):
    """ Divides lists in two sublists and then merges them according to their values (less value go first) """
    # divide list into two sublists
    left = _list[begin:middle+1]
    right = _list[middle+1:end+1]
    i, j = 0, 0
    # merge two sublists
    for k in range(begin, end+1):
        # if reach end of first sublist - merge the second list
        if i == len(left):
            _list[k] = right[j]
            j += 1
        # same for second sublist
        elif j == len(right):
            _list[k] = left[i]
            i += 1
        # else merge sublists according to their values
        else:
            if left[i] <= right[j]:
                _list[k] = left[i]
                i += 1
            elif right[j] < left[i]:
                _list[k] = right[j]
                j += 1


def merge_sort(_list, begin, end):
    """ Recursively divides and merges list with 'merge' function. Difficulty is O(n*lg(n)) """
    if begin < end:
        middle = divmod((begin + end), 2)[0]
        merge_sort(_list, begin, middle)
        merge_sort(_list, middle+1, end)
        merge(_list, begin, middle, end)


if __name__ == '__main__':
    _list = [7, 6, 3, 4, 2, 14, 5, 8, 1, 9, 6, 10]
    merge_sort(_list, 0, len(_list)-1)
    print(_list)
