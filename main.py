import sys

from stats import chars_dict_to_sorted_list, get_num_chars_dict, get_num_words


def get_book_text(book_path):
    with open(book_path) as book:
        book_text = book.read()
        return book_text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        num_words = get_num_words(book_text)
        num_chars_dict = get_num_chars_dict(book_text)
        chars_sorted_list = chars_dict_to_sorted_list(num_chars_dict)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in chars_sorted_list:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")


main()
