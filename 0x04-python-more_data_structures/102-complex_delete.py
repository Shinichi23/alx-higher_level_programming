#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())
    
    for v in list_keys:
        if v == a_dictionary.get(v):
            a_dictionary.pop(v)

    return a_dictionary
