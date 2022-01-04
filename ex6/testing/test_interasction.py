from ex6.intersection import read_input, find_intersection, get_intersection_result, func_diff, print_output
from pathlib import Path


def test_find_intersection(capfd):
    path = str(__file__).replace("\\" + Path(__file__).name, "\\files")
    for i in range(1, 7):
        print_output(path + f"\\input{i}.txt")
        out, err = capfd.readouterr()
        with open(path + f"\\output{i}.txt", "r") as expected:
            assert str(out).replace("\n", "") == expected.read()
