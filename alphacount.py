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
    parser = argparse.ArgumentParser(usage="./alphacount.py [options] <file>")

    parser.add_argument("file")
    parser.add_argument(
        "-c", metavar="CHAR", help="count occurences of a specific alphabetic character"
    )
    parser.add_argument("-r", action="store_true", help="sort in ascending order")
    args = parser.parse_args()
    try:
        text = get_text(args.file)
        num_chars = get_num_of_chars(text, args.c)
        char_list = convert_dict_to_list(num_chars, args.r)
        print_stats(char_list)
    except Exception as e:
        print(e)
        sys.exit(1)


main()
