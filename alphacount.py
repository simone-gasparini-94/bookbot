#!/usr/bin/env python3

import argparse
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
    parser = argparse.ArgumentParser()

    parser.add_argument("file")
    parser.add_argument("-c")
    args = parser.parse_args()
    try:
        text = get_text(args.file)
        num_chars = get_num_of_chars(text)
        char_list = convert_dict_to_list(num_chars)
        print_stats(char_list)
    except Exception as e:
        print(e)
        sys.exit(1)


main()
