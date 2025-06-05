def remove_long_strings_of_6(strings_list):
    for i in range(len(strings_list) -1, -1, -1):
        if len(strings_list[i]) > 6:
            strings_list.pop(i)