from ex3.testing.test_prime_decomposition import is_prime


def prime_closest(n):
    if is_prime(n):
        return n
    distance = 1
    candidate = 0
    while True:
        candidate = n - distance
        if candidate > 0 and is_prime(candidate):  # This wont call is_prime if candidate is negative!!
            return candidate
        candidate = n + distance
        if is_prime(candidate):
            return candidate
        distance += 1


def print_words_inf():
    # file = open("txt.input", "r")
    # text = file.read()
    text = "abra cadabra 1,2,3,4 houcus poucus 1,2,3"
    last_words_set = set()
    for word in text.split():
        missing_letters = []
        for c in word:
            if c not in last_words_set:
                missing_letters.append(c)
        print(f"{word:7}: {missing_letters}")
        last_words_set = last_words_set.union(set(word))


def reverse_list(lst):
    if lst == []:
        return []
    new_lst = [lst.pop()]
    new_lst += reverse_list(lst)
    return new_lst

