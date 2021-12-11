from random import *


def is_key_legal(key):
    if len(key) != 26:
        return False
    for c in key:
        if ord(c) < ord("a") or ord(c) > ord("z"):
            return False
    return True


def generate_key():
    key = "".join([chr(ord("a") + randint(0, 25)) for i in range(26)])
    return key


def encrypt(s, k):
    s = str(s).lower()
    encryption_dict = dict((chr(ord("a") + i), k[i]) for i in range(len(k)))
    encrypt_text = ""
    for i in range(len(s)):
        if s[i].isalpha():
            encrypt_text += encryption_dict[s[i]]
    return encrypt_text


def decrypt(s, k):
    s = str(s)
    decryption_dict = dict((k[i], chr(ord("a") + i)) for i in range(len(k)))
    decrypt_text = ""
    for i in range(len(s)):
        decrypt_text += decryption_dict[s[i]]
    return decrypt_text


def main():
    command = input("please type the next command: \"e\" (encryption) or \"d\" (decryption): ")
    if command == "e":
        key = generate_key()
        result = encrypt_from_user(key)
        if not result:
            return
        with open("key.txt", "w") as key_file:
            key_file.write(key)
        with open("ciphertext.txt", "w") as output_file:
            output_file.write(result)

    if command == "d":
        result = decrypt_from_user()
        if not result:
            return
        with open("decrypted.txt", "w") as output_file:
            output_file.write(result)


def decrypt_from_user(cipher_file_name="ciphertext.txt", key_file_name="key.txt"):
    key = ""
    try:
        with open(key_file_name, "r") as key_file:
            key = key_file.readline()
            if not is_key_legal(key):
                print(f"Key in \"{key_file_name}\" is illegal!")
                return False
        decrypted_lines = ""
        with open(cipher_file_name, "r") as input_file:
            for line in input_file.readlines():
                decrypted_lines += (decrypt(line, key))
        return decrypted_lines
    except IOError as e:
        print(f"Could not open file \"{e.filename}\"!")
        return False


def encrypt_from_user(key, plaintext_file_name="plaintext.txt"):
    encrypted_lines = ""
    try:
        with open(plaintext_file_name, "r") as input_file:
            for line in input_file.readlines():
                encrypted_lines += (encrypt(line, key))
        return encrypted_lines
    except IOError as e:
        print(f"Could not open file \"{e.filename}\"!")
        return False


if __name__ == '__main__':
    main()
