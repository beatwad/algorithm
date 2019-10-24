import math


def find_max_sublist_linear(_list):
    """ Find maximum sublist in linear time. Difficulty is O(n) """
    max_left = 0
    max_right = 0
    max_sum = -math.inf
    sub_sum = 0
    for i in range(0, len(_list)):
        if sub_sum < 0:
            if _list[i] > sub_sum:
                max_sum = _list[i]
                sub_sum = _list[i]
                max_left = i
                max_right = i
        else:
            sub_sum += _list[i]
            if sub_sum > max_sum:
                max_sum = sub_sum
                max_right = i
    return max_left, max_right, max_sum


if __name__ == '__main__':
    _list = [-13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(find_max_sublist_linear(_list))
