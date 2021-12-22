from ex5.print_sums import compute_results


def test_compute_result():
    path = str(__file__).replace("\\test_print_sums.py", "\\files")
    for i in range(1, 3):
        compute_results(path + f"\\input_ex2_{i}.txt", path + f"\\program_outputs\\output_ex2_{i}.txt")
        with open(path + f"\\output_ex2_{i}.txt") as src_output:
            with open(path + f"\\program_outputs\\output_ex2_{i}.txt") as output_to_check:
                assert output_to_check.read() == src_output.read()
