def print_sums_helper(n, lst, index, parts, writer):
    if n == 0:
        writer.write(str(sum(lst)) + " = " + " + ".join(map(str, lst)) + "\n")
        return
    if n < 0 or index >= len(parts):  # We encountered none existed combination
        return

    lst.append(parts[index])
    print_sums_helper(n - parts[index], lst, 0, parts, writer)
    lst.pop()
    print_sums_helper(n, lst, index + 1, parts, writer)


def print_sums_alt(n, parts, writer):
    print_sums_helper(n, [], 0, parts, writer)


