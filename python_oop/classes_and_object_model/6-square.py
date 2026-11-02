#!/usr/bin/env python3

"""Este modulo define una clase."""


class Square:
    """Esta clase representa un objeto de 4 lados."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa el cuadrado con validación de tipo y valor."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter: Recupera el valor de size"""
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

    @property
    def position(self):
        """Getter: Recupera el valor de position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter: Valida tipo y valor."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Imprime el cuadrado con # o una linea vacía"""
        print(self.__str__())

    def __str__(self):
        """Devuelve la representación del cuadrado."""
        if self.__size == 0:
            return ""

        lineas = []
        # Agrega saltos de línea verticales, position[1] (offset Y)
        for i in range(self.__position[1]):
            lineas.append("")

        # Agrega los espacios horizontales, position[0] (offset X) e imprime #
        for i in range(self.__size):
            lineas.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(lineas)
