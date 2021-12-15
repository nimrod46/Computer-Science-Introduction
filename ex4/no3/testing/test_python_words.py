from ex4.no3.python_words import main


def test_main(monkeypatch, capfd):
    for i in range(1, 6):
        path = str(__file__).replace("\\test_python_words.py", "\\files")
        monkeypatch.setattr('builtins.input', lambda _: path + f"\\my_prog{i}.py")
        main()
        with open(f"files\\python_words_output{i}.txt", "r") as file:
            output, err = capfd.readouterr()
            assert output == file.read()
