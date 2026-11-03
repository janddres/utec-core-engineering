#!/usr/bin/env python3

"""Este modulo define una clase."""


class Rectangle:
    """Esta clase representa un rectangulo."""

    def __init__(self, width=0, height=0):
        """Inicializa el rectangulo con validación de tipo y valor."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter: Recupera el valor de width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter: Valida tipo y valor."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter: Recupera el valor de heigth"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter: Valida tipo y valor."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
