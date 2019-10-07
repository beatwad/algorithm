def insertion_sort_recursive(_list: list) -> list:
    """ Recursively implements insertion sort algorithm with binary search of insertion place """
    if len(_list) == 1:
        return _list
    else:
        key = _list[-1]
        _list = insertion_sort_recursive(_list[:-1])
        # search index of value which is closest to key
        index = binary_search_recursive(_list, 0, len(_list)-1, key)
        # insert key into list according to it's value and index
        if _list[index] >= key:
            if index == 0:
                _list = [key] + _list
            else:
                _list = _list[0: index] + [key] + _list[index: len(_list)]
        else:
            _list = _list + [key]
        return _list


def binary_search_recursive(_list, begin, end, value):
    """ Recursively finds a value in sorted list using binary search """
    # if reach list size of 1 and this value isn't we looking for - return None
    if begin == end:
        if value != _list[begin]:
            return begin
    middle = divmod((begin + end), 2)[0]
    if value == _list[middle]:
        return middle
    elif value > _list[middle]:
        return binary_search_recursive(_list, middle+1, end, value)
    else:
        return binary_search_recursive(_list, begin, middle, value)


if __name__ == '__main__':
    a = [5, 4, 15, 3, 7, 6, 0, 2, 5, 1, 17, 8, 4, 2, 9, 1, 4]
    a = insertion_sort_recursive(a)
    print(a)
