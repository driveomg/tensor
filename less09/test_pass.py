"""Тест проверяет правильность работы фукнции проверки пароля"""

import passcheker

def test_good_pass_v1():
    assert passcheker.check('123q456') == True

def test_good_pass_v2():
    assert passcheker.check('Qwerty123') == True

def test_pass_less_6_symbol():
    assert passcheker.check('123q') == False

def test_pass_only_letters():
    assert passcheker.check('ABCDqwert') == False

def test_pass_only_digit():
    assert passcheker.check('12345123') == False


def test_pass_password_v1():
    assert passcheker.check('PaSsWoRd123') == False

def test_pass_password_v2():
    assert passcheker.check('11_password') == False

def test_pass_password_v3():
    assert passcheker.check('qwerPASSWORDqwer') == False   

