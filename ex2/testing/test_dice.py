from ex2.dice import main


def test_1(monkeypatch, capfd):
    monkeypatch.setattr('builtins.input', lambda _: "1000")
    main()
    out, err = capfd.readouterr()
    assert str(out).count("x") == 1000
