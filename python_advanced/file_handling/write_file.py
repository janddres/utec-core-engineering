#!/usr/bin/env python3
"""Module contenendor de la funcion write_file"""


def write_file(filename="", text=""):
    """Lee archivos de texto (UTF-8) y los imprime en el stdout."""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
