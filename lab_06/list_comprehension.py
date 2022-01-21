def multiply_lists(arr1, arr2):
    return [arr1[i] * arr2[i] for i in range(len(arr1))]


def mod_n_only(arr, n):
    return [i for i in arr if i % n == 0]


def how_many_below(arr, threshold):
    return sum([1 if i < threshold else 0 for i in arr])


def divide_list1(arr, num_of_inner_lists):
    inner_len = (len(arr) // num_of_inner_lists)
    return [[arr[j] for j in range(inner_len * i, inner_len * i + inner_len)] for i in range(num_of_inner_lists)]


def divide_list2(arr, num_of_inner_lists):
    inner_len = (len(arr) // num_of_inner_lists)
    return [[arr[j + i * inner_len] for j in range(inner_len)] for i in range(num_of_inner_lists)]


def create_matrix(size):
    return [[j for j in range(size)] for i in range(size)]


def make_list(n):
    return [[j for j in range(1, i + 1)] for i in range(1, n + 1)]


def flatten_matrix(mat):
    return [j for i in mat for j in i]


def flatten_lst6(mat):
    return [j for i in mat for j in i if len(j) < 6]


def word_len_list(s, w):
    return [len(i) for i in s.split() if i != w]


def max_list(lst1, lst2):
    return [lst1[i] if lst1[i] > lst2[i] else lst2[i] for i in range(len(lst1))]
