def matrix_multiply(matrix_1: list, matrix_2: list) -> list:
    rows = len(matrix_1)
    matrix_mult = list()
    for i in range(0, rows):
        temp_list = list()
        for j in range(0, rows):
            c = 0
            for k in range(0, rows):
                c += matrix_1[i][k]*matrix_2[k][j]
            temp_list.append(c)
        matrix_mult.append(temp_list)
    return matrix_mult


def matrix_multiply_recursive(matrix_a: list, matrix_b: list) -> list:
    rows = len(matrix_a)
    if rows == 1:
        matrix_mult = list()
        c = matrix_a[0][0]*matrix_b[0][0]
        matrix_mult.append([c])
    else:
        matrix_a_1_1, matrix_a_1_2, matrix_a_2_1, matrix_a_2_2 = divide_matrix_by_four(matrix_a)
        matrix_b_1_1, matrix_b_1_2, matrix_b_2_1, matrix_b_2_2 = divide_matrix_by_four(matrix_b)
        matrix_mult_1_1 = matrix_multiply_recursive(matrix_a_1_1, matrix_b_1_1) + \
                          matrix_multiply_recursive(matrix_a_1_2, matrix_b_2_1)
        matrix_mult_1_2 = matrix_multiply_recursive(matrix_a_1_1, matrix_b_1_2) + \
                          matrix_multiply_recursive(matrix_a_1_2, matrix_b_2_2)
        matrix_mult_2_1 = matrix_multiply_recursive(matrix_a_2_1, matrix_b_1_1) + \
                          matrix_multiply_recursive(matrix_a_2_2, matrix_b_2_1)
        matrix_mult_2_2 = matrix_multiply_recursive(matrix_a_2_1, matrix_b_1_2) + \
                          matrix_multiply_recursive(matrix_a_2_2, matrix_b_2_2)
        matrix_mult = join_matrix(matrix_mult_1_1, matrix_mult_1_2, matrix_mult_2_1, matrix_mult_2_2)
    return matrix_mult


def divide_matrix_by_four(matrix: list) -> (list, list, list, list):
    rows = len(matrix)
    rows_half = int(rows/2)
    matrix_1_1 = matrix[:rows_half]
    matrix_1_2 = matrix[:rows_half]
    matrix_2_1 = matrix[rows_half:]
    matrix_2_2 = matrix[rows_half:]
    for i in range(0, rows_half):
        matrix_1_1[i] = matrix_1_1[i][:rows_half]
        matrix_1_2[i] = matrix_1_2[i][rows_half:]
        matrix_2_1[i] = matrix_2_1[i][:rows_half]
        matrix_2_2[i] = matrix_2_2[i][rows_half:]
    return matrix_1_1, matrix_1_2, matrix_2_1, matrix_2_2


def join_matrix(matrix_1_1: list, matrix_1_2: list, matrix_2_1: list, matrix_2_2: list) -> list:
    rows = len(matrix_1_1)
    for i in range(0, rows):
        matrix_1_1[i] = matrix_1_1[i] + matrix_1_2[i]
        matrix_2_1[i] = matrix_2_1[i] + matrix_2_2[i]
    return matrix_1_1 + matrix_2_1


if __name__ == '__main__':
    # A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # B = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
    # print(matrix_multiply(A, B))

    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    B = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(matrix_multiply(A, B))
    print(matrix_multiply_recursive(A, B))
