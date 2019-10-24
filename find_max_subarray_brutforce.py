import math


def find_max_sublist_brute_force(_list):
    """ Find maximum sublis with brute force methon. Difficulty is O(n**2)"""
    max_left = 0
    max_right = 0
    max_sum = -math.inf
    for i in range(0, len(_list)):
        sub_sum = 0
        for j in range(i, len(_list)):
            sub_sum += _list[j]
            if sub_sum > max_sum:
                max_sum = sub_sum
                max_left = i
                max_right = j
    return max_left, max_right, max_sum


if __name__ == '__main__':
    _list = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(find_max_sublist_brute_force(_list))
