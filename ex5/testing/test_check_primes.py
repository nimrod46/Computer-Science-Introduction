from ex5.check_primes import compute_result


def test_compute_result():
    path = str(__file__).replace("\\test_check_primes.py", "\\files")
    for i in range(1, 5):
        compute_result(path + f"\\input_ex1_{i}.txt", path + f"\\program_outputs\\output_ex1_{i}.txt")
        with open(path + f"\\output_ex1_{i}.txt") as src_output:
            with open(path + f"\\program_outputs\\output_ex1_{i}.txt") as output_to_check:
                assert output_to_check.read() == src_output.read()
