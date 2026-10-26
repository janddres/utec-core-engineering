#!/usr/bin/env python3
"""Modulo para imprimir y devolver el ultimo digito de un numero."""


def print_last_digit(numero):
    """Imprime el ultimo digito de un numero y lo devuelve como positivo."""
    lastd = abs(numero) % 10
    print(lastd, end="")
    return lastd
