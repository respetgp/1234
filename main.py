import random

def chars_list_funktion (n=20): #->list[int]
    """Функция генерирует произвольный список из n элементов"""

    assert 2 < n < 100000
    assert type(n) == int

    chars_list_lokal = [random.randint(0, 10) for i in range(n)]

    return chars_list_lokal

def three_max_char_list (random_chars_list=chars_list_funktion()): #->list[int]
    """Функцию находит 3 максимальных уникальных числа из списка и возвращает их в порядке убывания"""

    assert len(random_chars_list) > 2
    assert type(random_chars_list) == list

    three_max_char = []
    random_chars_list = list(set(random_chars_list))
    for i in range(3):
        max_number = max(random_chars_list)
        three_max_char.append(max_number)
        random_chars_list.remove(max_number)

    return three_max_char


assert len(chars_list_funktion()) == 20
assert len(chars_list_funktion(3)) == 3
assert type(chars_list_funktion()) == list

assert len(three_max_char_list()) == 3
assert type(three_max_char_list()) == list
assert three_max_char_list([31, 8, 58, 70, 45, 39, 91, 29, 75, 49, 25, 84, 71, 68, 6, 8, 66, 96, 85, 58]) == [96,91,85]