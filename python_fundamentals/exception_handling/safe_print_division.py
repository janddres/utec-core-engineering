#!/usr/bin/env python3

def safe_print_division(a, b):
    c = None
    try:
        c = a/b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print("Inside result: {}".format(c))
    return c
