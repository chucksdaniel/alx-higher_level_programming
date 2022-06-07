#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    largest = 0
    for i in len(my_list) - 1:
        if  my_list[i] > largest:
            largest = my_list[i]

    return largest
