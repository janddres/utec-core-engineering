#!/usr/bin/env python3
"""Module contenendor de la funcion append_write"""


def append_write(filename="", text=""):
    """Escribe archivos de texto (UTF-8) y devuelve la cantidad de carac."""
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
