from merge_sort import merge_sort
from binary_search import binary_search_recursive


def search_for_two_values(_list, _sum):
    """ Search in list for two items whose sum is equal to parameter _sum. Difficulty is O(n*lg(n)) """
    # sort list by merge sort
    sorted_list = _list[:]
    merge_sort(sorted_list, 0, len(sorted_list)-1)
    for item in sorted_list:
        if item >= _sum:
            return None
        else:
            second_item = _sum - item
            # use binary search for searching for item in sorted list
            if binary_search_recursive(sorted_list, 0, len(sorted_list)-1, second_item):
                return {item: _list.index(item), second_item: _list.index(second_item)}
    return None


if __name__ == '__main__':
    _list = [5, 6, 2, 7, 2, 1, 11, 9, 1]
    print(search_for_two_values(_list, 20))




