""" 
Задача: Разработка сумматора
Условие: Суммирование неограниченных аргументов,
которые являются одним типом или могут быть приведены
к одному типу в самой функции(без доп. действий).
"""

import summator


def test_sum_digit_v1():
    assert summator.sum(20, -30) == -10.0

def test_sum_digit_v2():
    assert summator.sum(-300, -30, 11.1) == -318.9

def test_sum_str_v1():
    assert summator.sum('QWE', 'ЫЮЯ', '123') == 'QWEЫЮЯ123'

def test_sum_str_v2():
    assert summator.sum('222', '111', '123') == '222111123' 

def test_sum_list_v1():
    assert summator.sum([1], [2], [3]) == [[1], [2], [3]]


def test_sum_list_v2():
    assert summator.sum(['av'], [2], ['XYZ']) == [['av'], [2], ['XYZ']]