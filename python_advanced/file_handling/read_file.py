#!/usr/bin/env python3
"""Module contenendor de la funcion readfile"""


def read_file(filename=""):
    """Lee archivos de texto (UTF-8) y los imprime en el stdout."""
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
