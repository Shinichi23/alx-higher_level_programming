#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i, n in enumerate(my_list):
        if n == search:
            my_list[i] = replace
    return my_list
