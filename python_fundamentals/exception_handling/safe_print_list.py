#!/usr/bin/env python3

def safe_print_list(mi_lista=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{}".format(mi_lista[i]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return count
