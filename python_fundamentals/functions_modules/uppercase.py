#!/usr/bin/env python3

def uppercase(palabra):
    uppalabra = ''
    for i in palabra:
        if 97 <= ord(i) <= 122:
            let = ord(i) - 32
            uppalabra += chr(let)
        else:
            uppalabra += i

    return uppalabra
