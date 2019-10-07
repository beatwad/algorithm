from math import log2
from insertion_sort_recursive import insertion_sort_recursive


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


def merge_sort(_list, begin, end, min_len):
    """ Recursively divides and merges list with 'merge' function if list len is more than min_len parameter, else sort
    list by insertion sorting algorithm"""
    if len(_list[begin:end+1]) > min_len:
        middle = divmod((begin + end), 2)[0]
        merge_sort(_list, begin, middle, min_len)
        merge_sort(_list, middle+1, end, min_len)
        merge(_list, begin, middle, end)
    else:
        _list[begin:end+1] = insertion_sort_recursive(_list[begin:end+1])


def merge_sort_with_insertion(_list):
    """ Calculates min_len parameter by formula min_len = log2(len(_list)) and sorts that list """
    min_len = int(log2(len(_list)))
    print(min_len)
    merge_sort(_list, 0, len(_list)-1, min_len)


if __name__ == '__main__':
    _list = [7, 6, 3, 53, 2, 14, 5, 8, 1, 9, 6, 10, 4, 2, 13, 38, 3, 17, 21, 8, 0, 11, 3, 5, 19, 44, 2, 20, 12, 61, 76,
             23, 1, 4]
    print(len(_list))
    merge_sort_with_insertion(_list)
    print(_list)
