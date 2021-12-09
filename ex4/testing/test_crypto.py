from ex4 import crypto
from ex4.crypto import main, encrypt_from_user, decrypt_from_user, encrypt, decrypt


def test_is_key_legal():
    assert crypto.is_key_legal("groexuwtdmzvbjqkfnchliysap")
    assert not crypto.is_key_legal("groexuwDdmzvbjqkfnchliysap")
    assert not crypto.is_key_legal("groexuwdcdmzvbjqkfnchliysap")
    assert not crypto.is_key_legal("groexdmzvbjqkfnchliysap")


def test_generate_key():
    for i in range(10000):
        assert crypto.is_key_legal(crypto.generate_key())


def test_decrypt_from_user():
    with open("files\\decrypted1.txt", "r") as decrypted:
        assert decrypt_from_user("files\\ciphertext1.txt", "files\\key1.txt") == decrypted.readline()
    with open("files\\decrypted2.txt", "r") as decrypted:
        assert decrypt_from_user("files\\ciphertext2.txt", "files\\key2.txt") == decrypted.readline()


def test_encrypt_from_user():
    with open("files\\ciphertext1.txt", "r") as cipher:
        with open("files\\key1.txt", "r") as key:
            assert encrypt_from_user(key.readline(), "files\\plaintext1.txt") == cipher.readline()

    with open("files\\ciphertext2.txt", "r") as cipher:
        with open("files\\key2.txt", "r") as key:
            assert encrypt_from_user(key.readline(), "files\\plaintext2.txt") == cipher.readline()


def test_main(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "e")
    main()
    with open("key.txt", "r") as key_file:
        with open("ciphertext.txt", "r") as cipher_file:
            with open("plaintext.txt", "r") as plain_file:
                assert encrypt("".join(plain_file.readlines()), key_file.read()) == cipher_file.read()

    monkeypatch.setattr('builtins.input', lambda _: "d")
    main()
    with open("key.txt", "r") as key_file:
        with open("decrypted.txt", "r") as decrypted_file:
            with open("ciphertext.txt", "r") as cipher_file:
                assert decrypt("".join(cipher_file.readlines()), key_file.read()) == decrypted_file.read()


