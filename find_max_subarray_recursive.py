import math


def find_max_sublist(_list, low, high):
    """ Recursively find max sublist of list. Difficulty is O(n*lg(n)) """
    if low == high:
        return low, high, _list[low]
    else:
        mid = divmod(low + high, 2)[0]
        left_low, left_high, left_sum = find_max_sublist(_list, low, mid)
        right_low, right_high, right_sum = find_max_sublist(_list, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_sublist(_list, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def find_max_crossing_sublist(_list, low, mid, high):
    """ Find max sublist which is contained by list and crosses it's middle """
    max_left = 0
    max_right = 0
    left_sum = -math.inf
    _sum = 0
    for index in range(mid, low-1, -1):
        _sum += _list[index]
        if _sum > left_sum:
            left_sum = _sum
            max_left = index
    right_sum = -math.inf
    _sum = 0
    for index in range(mid+1, high+1):
        _sum += _list[index]
        if _sum > right_sum:
            right_sum = _sum
            max_right = index
    return max_left, max_right, left_sum+right_sum


if __name__ == '__main__':
    _list = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(find_max_sublist(_list, 0, len(_list)-1))
