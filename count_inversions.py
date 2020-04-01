def count_inversions(_list, begin, middle, end):
    """ Divides lists in two sublists and then merges them according to their values (less value go first) and count
    inversions number """
    # divide list into two sublists
    merge_count = 0
    left = _list[begin:middle+1]
    right = _list[middle+1:end+1]
    i, j = 0, 0
    # merge two sublists
    for k in range(begin, end+1):
        # if reach end of left sublist - merge the second list
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
                merge_count += (len(left) - i)
    return merge_count


def merge_count_inversions(_list, begin, end):
    """ Recursively divides and merges list with 'merge' function and count inversions number 5"""
    merge_count = 0
    if begin < end:
        middle = divmod((begin + end), 2)[0]
        merge_count += merge_count_inversions(_list, begin, middle)
        merge_count += merge_count_inversions(_list, middle+1, end)
        merge_count += count_inversions(_list, begin, middle, end)
    return merge_count


if __name__ == '__main__':
    _list = [7, 8, 6, 5, 4, 3, 8, 7, 2, 1]
    inversions = merge_count_inversions(_list, 0, len(_list)-1)
    print(inversions)
