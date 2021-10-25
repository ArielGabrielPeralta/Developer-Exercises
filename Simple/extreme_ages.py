from random import randint


def register():
    """
    Genera una lista de diccionarios, los cuales contienen el Id y la Edad de la persona, la edad será un
    número aleatorio del 1 al 100.
    :return: Lista de diez diccionarios
    Test:
    >>> people_list = register()
    >>> len(people_list)
    10
    """
    people_list = list()
    _id = 0
    while len(people_list) < 10:
        age = randint(1, 100)
        people_list.append({'Id': _id,
                            'Age': age})
        _id += 1
    return people_list


def order_people(people_list):
    """
    Ordena la lista de diccionarios que recibe por parámetros según las edades.
    :param people_list:
    :return: La lista de diccionarios ordenadas por edades, de mayor a menor.
    """
    age_list = list()
    order_people = list()
    for person in people_list:
        if person['Age'] not in age_list:
            age_list.append(person['Age'])
    age_list.sort(reverse=True)
    for age in age_list:
        for person in people_list:
            if age == person['Age']:
                order_people.append(person)
    young = order_people[-1]['Id']
    old = order_people[0]['Id']
    print('La persona más joven tiene el Id {}.'.format(young))
    print('La persona más vieja tiene el Id {}.'.format(old))
    return order_people


if __name__ == '__main__':
    import doctest

    doctest.testmod()
