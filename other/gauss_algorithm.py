def get_canonical_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    i = 0
    j = 0
    while i < m and j < n:
        if matrix[i][j] == 0:
            if not try_replace_row_with_none_leading_zero(matrix, i, j):
                j += 1
        else:
            change_pivot_to_one(matrix, i, j)
            zero_column_by_pivot(matrix, i, j)
            i += 1
            j += 1

    return matrix


def try_replace_row_with_none_leading_zero(matrix, i, j):
    while matrix[i][j] == 0:
        for k in range(i + 1, len(matrix)):
            if matrix[k][j] != 0:
                matrix = swap_matrix_rows(matrix, i, k)
                break
        if matrix[i][j] == 0:
            break

    return matrix[i][j] != 0


def swap_matrix_rows(matrix, src_row_num, dest_row_num):
    src_row = matrix[src_row_num]
    matrix[src_row_num] = matrix[dest_row_num]
    matrix[dest_row_num] = src_row
    return matrix


def change_pivot_to_one(matrix, i, j):
    matrix[i] = multiply_row_by_scalar(matrix[i], 1 / matrix[i][j])
    return matrix


def zero_column_by_pivot(matrix, i, j):
    for row_index in range(0, len(matrix)):
        if row_index == i:
            continue

        scaled_pivot_row = multiply_row_by_scalar(matrix[i], matrix[row_index][j])
        matrix[row_index] = subtract_rows(matrix[row_index], scaled_pivot_row)
    return matrix


def multiply_row_by_scalar(row, scalar):
    scaled_row = list(row)
    for k in range(0, len(scaled_row)):
        scaled_row[k] *= scalar
    return scaled_row


def subtract_rows(row1, row2):
    subtracted_row = list(row1)
    for k in range(0, len(row1)):
        subtracted_row[k] = row1[k] - row2[k]
    return subtracted_row


print(get_canonical_matrix([[1,-2,0,2],
                            [2,2,2,1]]))

# print(get_canonical_matrix([[No1, 3, No1, 9],
#                             [No1, No1, -No1, No1],
#                             [3, 11, 5, 35]]))
#
# print(get_canonical_matrix([[2, No1, -No1, 8],
#                             [-3, -No1, 2, -11],
#                             [-2, No1, 2, -3]]))
#
# print(get_canonical_matrix([[No1, 0, 0, 0],
#                             [0, No1, 0, 0],
#                             [0, 0, No1, 0]]))
#
# print(get_canonical_matrix([[0, 2, 2, No1 / 3.0,],
#                             [0, -5, 10, 5 / 3.0],
#                             [-3, 6, 0, -No1]]))
#
# print(get_canonical_matrix([[0, 2, 2, -No1, 6, 4],
#                             [0, 4, 4, No1, 10, 13],
#                             [0, 8, 8, -No1, 26, 23]]))
