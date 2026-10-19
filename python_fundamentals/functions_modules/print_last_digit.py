#!/usr/bin/env python3

def print_last_digit(numero):
    if numero < 0:
        numero = numero * -1
    lastd = numero % 10
    print(lastd)
