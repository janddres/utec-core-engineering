#!/usr/bin/env python3

"""Este modulo define una clase."""


class Square:
    """Esta clase representa un objeto de 4 lados."""

    def __init__(self, size=0):
        """Inicializa el cuadrado con validación de tipo y valor."""
        if not isinstance(size, int):
            raise TypeError("El valor ingresado debe ser un entero")
        if size < 0:
            raise ValueError("El valor ingresado debe ser >= 0")
        
        self.__size = size
