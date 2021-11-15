from ex2.arithmetic import *


def test_1():
    assert arithmetic_find([12, 33, 54, 3, 7, 11, 15, 13, 11, 9, 7, 5, 10, 15, 20, 25]) == 6


def test_2():
    assert arithmetic_find([123, 2, 5, 4, 8, 4, 5, 5, 7]) == 0


def test_main(monkeypatch, capfd):
    monkeypatch.setattr('builtins.input', lambda _: "12, 33, 54, 3, 7, 11, 15, 13, 11, 9, 7, 5, 10, 15, 20, 25")
    main()
    out, err = capfd.readouterr()
    assert out == "Longest arithmetic sequence: 15, 13, 11, 9, 7, 5"
