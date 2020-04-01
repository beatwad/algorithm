def binary_search_recursive(_list, begin, end, value):
    """ Recursively finds a value in sorted list using binary search """
    # if reach list size of 1 and this value isn't we looking for - return None
    if begin == end:
        if value != _list[begin]:
            return None
    middle = divmod((begin + end), 2)[0]
    if value == _list[middle]:
        return middle
    elif value > _list[middle]:
        return binary_search_recursive(_list, middle+1, end, value)
    else:
        return binary_search_recursive(_list, begin, middle, value)

x = 'dfasfs'

if __name__ == '__main__':
    _list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    index = binary_search_recursive(_list, 0, len(_list)-1, 9)
    print(index)
