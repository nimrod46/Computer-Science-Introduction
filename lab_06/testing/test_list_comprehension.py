from lab_06.list_comprehension import *


def test_multiply_lists():
    assert multiply_lists([1, 2, 3], [1, 2, 3]) == [1, 4, 9]


def test_mod_n_only():
    assert mod_n_only([1, 2, 3, 4, 5, 6, 7], 3) == [3, 6]


def test_how_many_below():
    assert how_many_below([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 4


def test_divide_list1():
    assert divide_list1([78, 57, 45, 4, 43, 45, 34, 12], 4) == [[78, 57], [45, 4], [43, 45], [34, 12]]


def test_divide_list2():
    assert divide_list2([78, 57, 45, 4, 43, 45, 34, 12], 4) == [[78, 57], [45, 4], [43, 45], [34, 12]]


def test_creat_matrix():
    assert create_matrix(3) == [[0, 1, 2], [0, 1, 2], [0, 1, 2]]


def test_make_list():
    assert make_list(3) == [[1], [1, 2], [1, 2, 3]]


def test_flatten_matrix():
    assert flatten_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_flatten_lst6():
    assert flatten_lst6(
        [["Mercury", "Venus", "Earth"], ["Mars", "Jupiter", "Saturn"], ["Uranus", "Neptune", "Pluto"]]) == ["Venus",
                                                                                                            "Earth",
                                                                                                            "Mars",
                                                                                                            "Pluto"]


def test_word_len_list():
    assert word_len_list("the quick brown fox jumps over the lazy dog", "the") == [5, 5, 3, 5, 4, 4, 3]


def test_max_list():
    assert max_list([2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2]) == [2, 2, 2, 2, 2, 2]
