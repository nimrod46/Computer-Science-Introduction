"""
Student: Nimrod Machlav
ID: 315230185
Assignment no. 4
Program: python_words.py
"""

import keyword


def remove_from_string(s, start, end):
    """
    Removing all sub strings of "s" between "start" and "end" strings
    :return: Original string without the specified sub strings
    """
    s = str(s)
    new_string = ""
    next_start_index = s.find(start)
    end_index = s.find(end, next_start_index + 1)
    while end_index != -1 and next_start_index != -1:
        new_string += s[:next_start_index]
        s = s[end_index + len(end):]
        next_start_index = s.find(start)
        end_index = s.find(end, next_start_index + 1)
    return new_string + s


def split_all(s, str_lst):
    """
    Splits "s" by all string in "str_lst"
    :return: List of all splitted string from "s"
    """
    splitted_list = [s]
    for word in str_lst:
        new_splitted_list = []
        for text in splitted_list:
            new_splitted_list += text.split(word)
        splitted_list = new_splitted_list
    return [i for i in splitted_list if i != ""]


def main():
    """
    Asks the user for a python file name and prints all occurrences of python keywords and their occurrences count
    """
    try:
        with open(input("Enter file name:"), "r") as file:
            text = file.read()
            text = remove_from_string(text, '"""', '"""')
            text = remove_from_string(text, '"', '"')
            text = remove_from_string(text, '#', '\n')
            texts = split_all(text, [" ", "*", ",", "-", "+", ".", "[", "]", "==", "=", ")", "(", ":", "\n\n", "\n", ";"])
            keywordList = keyword.kwlist
            for word in keywordList:
                count = texts.count(word)
                if count != 0:
                    print(f"{word:6} : {count}")
    except IOError as e:
        print(f"Could not found file {e.filename}")


if __name__ == '__main__':
    main()
