def get_num_words(book_text):
    num_words = book_text.split()
    return len(num_words)


def get_num_chars_dict(book_text):
    num_chars_dict = {}
    chars = list(book_text.lower())
    for char in chars:
        if char not in num_chars_dict:
            num_chars_dict[char] = 0
        num_chars_dict[char] += 1
    return num_chars_dict


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = list()
    for char in num_chars_dict:
        if char.isalpha():
            sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
