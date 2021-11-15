from ex2.triangle import *


def test_1(monkeypatch, capfd):
    responses = iter(['9', '5', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    main()
    out, err = capfd.readouterr()
    assert str(out).count("*") == 32 and str(out).count("$") == 7 * 5
