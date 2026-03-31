#!/usr/bin/env python3

import sys

from stats import (
    convert_dict_to_list,
    get_num_of_chars,
    print_stats,
)


def get_text(path):
    with open(path, encoding="utf-8-sig") as file:
        return file.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    try:
        text = get_text(path)
        num_chars = get_num_of_chars(text)
        char_list = convert_dict_to_list(num_chars)
        print_stats(char_list)
    except Exception as e:
        print(e)
        sys.exit(1)


main()
