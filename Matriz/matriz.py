import random
from pprint import pprint


def create_matriz():
    random.seed()
    matriz = [None] * 5
    for column in range(5):
        matriz[column] = [None] * 5
    for row in range(len(matriz)):
        for column in range(len(matriz[row])):
            matriz[row][column] = random.randint(0, 9)
    pprint(matriz)



create_matriz()
