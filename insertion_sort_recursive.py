def insertion_sort_recursive(_list: list) -> list:
    """ Recursively implements insertion sort algorithm. Difficulty is O(n**2)"""
    if len(_list) == 1:
        return _list
    else:
        key = _list[-1]
        _list = insertion_sort_recursive(_list[:-1])
        _list.append(key)
        i = len(_list) - 2
        while i >= 0 and _list[i] > key:
            _list[i + 1] = _list[i]
            i -= 1
        _list[i + 1] = key
        return _list


if __name__ == '__main__':
    a = [5, 4, 15, 3, 7, 6, 0, 2]
    a = insertion_sort_recursive(a)
    print(a)
