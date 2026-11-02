#!/usr/bin/env python3

"""Este modulo define una clase."""


class Square:
    """Esta clase representa un objeto de 4 lados."""

    def __init__(self, size=0):
        """Inicializa el cuadrado con validación de tipo y valor."""
        self.size = size

    @property
    def size(self):
        """Getter: Recupera el valor del tamaño."""
        return self.__size

    @size.setter
    def size(self, size_set):
        """Setter: Valida tipo y valor."""
        if not isinstance(size_set, int):
            raise TypeError("size must be an integer")
        if size_set < 0:
            raise ValueError("size must be >= 0")
        self.__size = size_set

    def area(self):
        return (self.__size * self.__size)

