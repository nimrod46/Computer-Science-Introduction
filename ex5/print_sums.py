def print_sums_helper(n, s, parts, writer):
    """
    Writes all sum combinations of "n" by all numbers in "parts" list into "writer" file using "s"
    as a string storage for all previous additions
    """
    if n == 0:
        writer.write(s[:-2] + "\n")
        return
    if n < 0:  # We encountered a nonexistent combination
        return

    for i in parts:
        print_sums_helper(n - i, s + f" {i} +", parts, writer)


def print_sums(n, parts, writer):
    """
    Uses "print_sums_helper" while inserting a line prefix (such as: "6 =" when n=6)
    to write all sub sum combinations of "n" by all numbers in "parts" list into "writer" file
    """
    print_sums_helper(n, f"{n} =", parts, writer)


def try_parse_numbers_list(numbers):
    """
    Tries to parse numbers list as a valid input, will fail if:
    1. Duplicate numbers are presents in the combinations part
    2. None positive integers numbers are presents
    3. Less then 2 numbers are presents in each row
    :return: True if parsing succeeded, else False
    """
    for i in range(len(numbers)):
        if not numbers[i].isdigit() or int(numbers[i]) < 1:
            return False
        numbers[i] = int(numbers[i])

    return len(numbers[1:]) == len(set(numbers[1:])) and len(numbers) >= 2


def compute_results(src_file_name, dest_file_name):
    """
    Writes the result of "print_sums" based on "src_file_name" as input file into "dest_file_name" file,
    "Error" will be writen if parsing a line failed
    """
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
    """
    Calls "compute_results" to read from "input_ex2.txt" into "output_ex2.txt"
    """
    compute_results("input_ex2.txt", "output_ex2.txt")


if __name__ == '__main__':
    main()
