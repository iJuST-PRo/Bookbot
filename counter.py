import sys, getopt


def main(argv):
    try:
        book_path = argv
        text = get_text(book_path)
        num_words = word_count(text)
        chars_count_dict = chars_counter(text)
        fully_sorted = sort_chars(chars_count_dict)
        print(f'----- Begin Report of {book_path} -----')
        print(f'{num_words} words found in the book\n')
        for i in fully_sorted:
            if not i['chars'].isalpha():
                continue
            print(f"letter {i['chars']} was found {i['num']}")
        print('\n----- End Report -----')
    except:
        print('Error: The file name/path is incorrect or the file is unreadable')


def sort_chars(chars_count_dict):
    sorted_chars = []
    for ch in chars_count_dict:
        sorted_chars.append({"chars":ch, "num":chars_count_dict[ch]})
    sorted_chars.sort(reverse=True, key=lambda d: d['num'])
    return sorted_chars


def chars_counter(text):
    chars = {}
    for i in text:
        lowered = i.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def word_count(text):
    words = text.split()
    return len(words)


def get_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except:
        print(f'Usage: python {sys.argv[0]} <file>')