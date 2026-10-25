#!/usr/bin/env python3

def raise_exception():
    a = 2
    b = "Andres"
    try:
        c = a/b
    except TypeError as e:
        print("Error de tipo: {}".format(e))
