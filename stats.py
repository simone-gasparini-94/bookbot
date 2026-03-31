def get_num_of_chars(string):
    chars = {}
    for char in string:
        lower_case = char.lower()
        if lower_case not in chars:
            chars[lower_case] = 1
            continue
        chars[lower_case] += 1
    return chars


def sort_on(items):
    return list(items.values())[0]


def convert_dict_to_list(dict):
    list = []
    for key in dict:
        list.append({key: dict[key]})
        list.sort(reverse=True, key=sort_on)
    return list


def print_stats(chars):
    for char in chars:
        for key in char:
            if key.isalpha():
                print(f"{key}: {char[key]}")
