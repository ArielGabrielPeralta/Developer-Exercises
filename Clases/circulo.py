from math import pi


class Circulo:
    """
    >>> circulo_1 = Circulo(5)
    >>> print(circulo_1.area())
    78.53981633974483
    >>> print(circulo_1.perimeter())
    31.41592653589793
    >>> circulo_2 = circulo_1 * 3

    >>> circulo_1.set_radio(6)
    >>> print(circulo_1.area())
    113.09733552923255
    >>> print(circulo_1.perimeter())
    37.69911184307752
    >>> circulo_3 = circulo_1 * 2
    """

    def __init__(self, radio):
        """
        Cuando se instancia la clase el atributo radio debe ser mayor que 0
        :param radio:
        """
        self.__radio = radio
        if self.__radio <= 0:
            raise ValueError('\033[1;31;40m El Radio del Circulo no puede ser igual o inferior a cero \033[0;m')

    def area(self):
        """
        Se calcula el area del circulo.
        :return: area del circulo.
        """
        area = (pi * (self.__radio ** 2))
        return area

    def perimeter(self):
        """
        Se calcula el perimetro del circulo.
        :return: perimetro del circulo.
        """
        perimeter = 2 * pi * self.__radio
        return perimeter

    def set_radio(self, value):
        """
        Se modifica el radio del circulo.
        :param value: nuevo radio
        :return: el radio modificado.
        """
        if value <= 0:
            raise ValueError('\033[1;31;40m El Radio del Circulo no puede ser igual o inferior a cero \033[0;m')
        else:
            self.__radio = value
        return

    def __mul__(self, n):
        """
        Cuando se multiplica el objeto, lo hace sobre el atributo radio, y retorna otro objeto Circulo con el
        radio modificado.
        :param n: numero a multiplicar por el objeto.
        :return: un objeto Circulo con el radio ya multiplicado.
        """
        if n <= 0:
            raise ValueError(
                '\033[1;31;40m No se puede multiplicar el Radio por valores iguales o inferiores a 0 \033[0;m')
        return Circulo(self.__radio * n)

    def __str__(self):
        return """ \033[1;32;40m El Circulo tiene un radio de {} unidades.'\n' Su Area es de {} unidades cuadradas.'\n' Su Perimetro es {} unidades. \033[0;m""".format(
            self.__radio, round(self.area(), 2), round(self.perimeter(), 2))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
