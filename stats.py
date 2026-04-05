def get_count_char(string, character):
    if not character.isalpha():
        raise Exception(f"Error: {character} is not an alphabetic character")
    count = 0
    for char in string:
        lower_case = character.lower()
        if lower_case == char.lower():
            count += 1
    return {character: count}


def get_num_of_chars(string, character):
    if character is not None:
        return get_count_char(string, character)
    chars = {}
    for char in string:
        if not char.isalpha():
            continue
        lower_case = char.lower()
        if lower_case not in chars:
            chars[lower_case] = 1
            continue
        chars[lower_case] += 1
    return chars


def sort_on(items):
    return list(items.values())[0]


def convert_dict_to_list(char_dict, ascending):
    char_list = []
    for key in char_dict:
        char_list.append({key: char_dict[key]})
    if not ascending:
        char_list.sort(reverse=True, key=sort_on)
    else:
        char_list.sort(reverse=False, key=sort_on)
    return char_list


def print_stats(chars):
    for char in chars:
        for key in char:
            print(f"{key}: {char[key]}")
