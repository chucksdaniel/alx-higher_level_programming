#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list), -1):
        print("{:d}".format(my_list[i]))

if __name__ == '__main__':
    my_list = [2, 4, 6, 8]
    print_reversed_list_integer(my_list)
