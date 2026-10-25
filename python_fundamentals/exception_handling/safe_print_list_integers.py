#!/usr/bin/env python3

def safe_print_list_integers(mi_lista=[], x=0):

    count = 0
    for i in range(x):
        try:
            print("{:d}".format(mi_lista[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count
