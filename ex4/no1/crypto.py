from random import *


def is_key_legal(key):
    """
    Validating a given key
    :param key: Key to validate
    :return: True if the given key is legal, otherwise False
    """
    if len(key) != 26:
        return False
    for c in key:
        if ord(c) < ord("a") or ord(c) > ord("z"):
            return False
    return True


def generate_key():
    """
    Generates a random key
    :return: Random key
    """
    key = "".join([chr(ord("a") + randint(0, 25)) for i in range(26)])
    return key


def encrypt(s, k):
    """
    Encrypt a given sting {s} by a given {k} using substitution cipher
    :param s: Text to encrypt
    :param k: Substitution cipher key
    :return: Encrypted text
    """
    s = str(s).lower()
    encryption_dict = dict((chr(ord("a") + i), k[i]) for i in range(len(k)))
    encrypt_text = ""
    for i in range(len(s)):
        if s[i].isalpha():
            encrypt_text += encryption_dict[s[i]]
    return encrypt_text


def decrypt(s, k):
    """
    Decrypt a given string "s" by a given "k" using substitution cipher
    :param s: Text to Decrypt
    :param k: Substitution cipher key
    :return: Decrypted text
    """
    s = str(s)
    decryption_dict = dict((k[i], chr(ord("a") + i)) for i in range(len(k)))
    decrypt_text = ""
    for i in range(len(s)):
        decrypt_text += decryption_dict[s[i]]
    return decrypt_text


def main():
    """
    Main logic func, asks the user for a command and creates the desired file containing the output
    """
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
    """
    Decrypt a cipher file by a given key
    :param cipher_file_name: For testing, an optional input cipher file name
    :param key_file_name: For testing, an optional input key file name
    :return: The decrypted text
    """
    try:
        with open(key_file_name, "r") as key_file:
            key = key_file.readline()
            if not is_key_legal(key):
                print(f"Key in \"{key_file_name}\" is illegal!")
                return False
        decrypted_text = ""
        with open(cipher_file_name, "r") as input_file:
            for line in input_file.readlines():
                decrypted_text += (decrypt(line, key))
        return decrypted_text
    except IOError as e:
        print(f"Could not open file \"{e.filename}\"!")
        return False


def encrypt_from_user(key, plaintext_file_name="plaintext.txt"):
    """
    Encrypt plain text file using a given key
    :param key: A given key to encrypt with
    :param plaintext_file_name: For testing, an optional input text file name
    :return: The encrypted text
    """
    encrypted_text = ""
    try:
        with open(plaintext_file_name, "r") as input_file:
            for line in input_file.readlines():
                encrypted_text += (encrypt(line, key))
        return encrypted_text
    except IOError as e:
        print(f"Could not open file \"{e.filename}\"!")
        return False


if __name__ == '__main__':
    main()
