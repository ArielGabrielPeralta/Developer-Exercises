import random


# from pprint import pprint


def create_matriz():
    """
    Crea una matriz vacía y la retorna.
    :return: matriz 5 x 5 con valores None.
    >>> create_matriz()
    [[None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None]]
    """
    random.seed()
    matriz = [None] * 5
    for column in range(5):
        matriz[column] = [None] * 5
    return matriz


def fill_matriz(matriz):
    """
    Rellena la matriz vacía con valores random, se recomienda que sean 0 y 1 para que haya mas posibilidades
    de matchear.
    :param matriz: matriz vacía.
    :return: matriz con valores random.
    """
    for row in range(len(matriz)):
        for column in range(len(matriz[row])):
            matriz[row][column] = random.randint(0, 1)
    # pprint(matriz)
    return


def search_sequence(matriz):
    """
    Busca por fila y columna secuencias de 4 numeros consecutivos, ya sea en vertical como en horizontal.
    Si sucede que coinciden 4 números, solo tomará los primeros 4.
    :param matriz:
    Test:
    >>> matriz = [[1, 0, 1, 0, 0],[0, 1, 1, 0, 0],[1, 1, 1, 1, 0],[0, 1, 0, 0, 0],[0, 0, 0, 0, 0]]
    >>> search_sequence(matriz)
    Buscando mach por fila
    Hay match sobre la fila 2, arranca en el indice (2, 0) y termina en el (2, 3)
    Hay match sobre la fila 4, arranca en el indice (4, 0) y termina en el (4, 3)
    Buscando mach por columna
    Hay match sobre la columna 4, arranca en el indice (0, 4) y termina en el (3, 4)
    """
    print('Buscando mach por fila')
    match_row = 0
    for row in range(len(matriz)):
        for column in range(len(matriz[row])):
            count = 0
            init = None
            end = None
            number = matriz[row][column]
            for i in range(len(matriz[row])):
                if matriz[row][i] == number and count == 0:
                    count += 1
                    init = (row, i)
                elif matriz[row][i] == number and count == 3:
                    count += 1
                    end = (row, i)
                elif matriz[row][i] == number and count != 4:
                    count += 1
                elif count == 4:
                    continue
                else:
                    count = 0
            if count == 4:
                print("Hay match sobre la fila {}, arranca en el indice {} y termina en el {}".format(row, init, end))
                match_row += 1
                break
    print('Buscando mach por columna')
    match_column = 0
    for i in range(len(matriz)):
        for row in matriz:
            number = row[i]
            count = 0
            init = None
            end = None
            for j in range(len(matriz)):
                if matriz[j][i] == number and count == 0:
                    count += 1
                    init = (j, i)
                elif matriz[j][i] == number and count == 3:
                    count += 1
                    end = (j, i)
                elif matriz[j][i] == number and count != 4:
                    count += 1
                elif count == 4:
                    continue
                else:
                    count = 0
            if count == 4:
                print("Hay match sobre la columna {}, arranca en el indice {} y termina en el {}".format(i, init, end))
                match_column += 1
                break
    if match_column == 0:
        print('No se encontraron coincidencias en las columnas')
    if match_row == 0:
        print('No se encontraron coincidencias en las filas')
    return


if __name__ == '__main__':
    import doctest

    doctest.testmod()
