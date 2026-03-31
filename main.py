def get_book_text(path):
    with open(path) as file:
        return file.read()


def main():
    frankenstein_path = "./books/frankenstein.txt"
    print(get_book_text(frankenstein_path))


main()
