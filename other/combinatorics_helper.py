cache = set()


def helper_get_num_of_variations(seq: list, word, remove_items, finished, excluding):
    if finished(word):
        print(word)
        return 1

    if word not in cache:
        cache.add(word)
    else:
        return 0

    count = 0
    for i in range(len(seq)):
        if remove_items:
            a = seq.pop(i)
        else:
            a = seq[i]

        w = str(word + str(a))
        if excluding(w):
            count += helper_get_num_of_variations(seq, w, remove_items, finished, excluding)
        if remove_items:
            seq.insert(i, a)
    return count


def get_num_of_variations(seq: list, remove_items, finished, excluding):
    cache.clear()
    helper_get_num_of_variations(seq, "", remove_items, finished, excluding)


def _5_digit_num_left_to_right_order():
    def legal_num(x):
        if x[0] != "1":
            return False
        for i in range(len(x) - 1):
            if int(x[i]) >= int(x[i + 1]):
                return False
        return True

    def finished(x):
        return len(x) == 5

    print(
        get_num_of_variations(["1", "2", "3", "4", "5", "6", "7", "8", "9"], False, finished, legal_num))


# noinspection PyPep8Naming
def only_one_AA_in_text():
    def legal(x):
        if x.find("AAA") == -1 and x.find("AAAA") == -1 and x.find("AAAAA") == -1:
            first = x.find("AA")
            if first != -1 and x.find("AA", first + 1) != -1:
                return False
            return True
        return False

    def finished1(x):
        if x.find("AA") != -1 and len(x) == 11:
            return True
        return False

    print(get_num_of_variations(["A", "A", "A", "A", "A", "B", "B", "R", "R", "C", "D"], True, finished1, legal))
