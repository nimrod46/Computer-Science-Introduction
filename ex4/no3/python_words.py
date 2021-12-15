import keyword


def remove_from_string(s, start, end):
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
    splitted_list = [s]
    for keyword in str_lst:
        new_splitted_list = []
        for text in splitted_list:
            if text == '':
                continue
            new_splitted_list += text.split(keyword)
        splitted_list = new_splitted_list
    return splitted_list


def main():
    try:
        with open(input("Enter file name:"), "r") as file:
            text = file.read()
            text = remove_from_string(text, '"""', '"""')
            text = remove_from_string(text, '"', '"')
            text = remove_from_string(text, '#', '\n')
            texts = split_all(text, [" ", ".", "[", "]", "==", "=", ")", "(", ":", "\n\n", "\n", ";"])
            keywordList = keyword.kwlist
            for word in keywordList:
                count = texts.count(word)
                if count != 0:
                    print(f"{word:6} : {count}")

    except IOError as e:
        print(f"Could not found file {e.filename}")


if __name__ == '__main__':
    main()
