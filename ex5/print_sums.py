def print_sums_helper(n, s, parts, writer):
    if n == 0:
        writer.write(s[:-2] + "\n")
        return
    if n < 0:
        return

    for i in parts:
        print_sums_helper(n - i, s + f" {i} +", parts, writer)


def print_sums(n, parts, writer):
    print_sums_helper(n, f"{n} =", parts, writer)


def try_parse_numbers_list(numbers):
    for i in range(len(numbers)):
        if not numbers[i].isdigit() or int(numbers[i]) < 1:
            return False
        numbers[i] = int(numbers[i])
    return len(numbers) == len(set(numbers)) >= 2


def compute_results(src_file_name, dest_file_name):
    with open(src_file_name, "r") as src_file:
        with open(dest_file_name, "w") as dst_file:
            for line in src_file.readlines():
                numbers = line.split()
                if try_parse_numbers_list(numbers):
                    dst_file.write(f"{numbers[0]} as sum of ")
                    if len(numbers) > 2:
                        dst_file.write(", ".join(map(str, numbers[1:-1])))
                        dst_file.write(f" and {numbers[-1]}:\n")
                    else:
                        dst_file.write(f"{numbers[1]}:\n")

                    print_sums(numbers[0], numbers[1:], dst_file)
                    dst_file.write("\n")
                else:
                    dst_file.write(f"{line}")
                    dst_file.write(f"Error\n\n")


def main():
    compute_results("input_ex2.txt", "output_ex2.txt")


if __name__ == '__main__':
    main()

