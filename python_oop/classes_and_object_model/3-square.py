#!/usr/bin/env python3

"""Este modulo define una clase."""


class Square:
    """Esta clase representa un objeto de 4 lados."""

    def __init__(self, size=0):
        """Inicializa el cuadrado con validación de tipo y valor."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
