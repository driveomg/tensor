
"""
    Функция получает  аргументы и суммирует их. 
    Функция возвращает только сумму без форматирования.
    Принимаются только списки, строки и цифры.
    Функция принимает строго аргументы одного типа.

"""


def sum(*args):
    err = 'Поддерживается суммирование переменных только одного типа'
    rez = '' 
    digitTrigger = False

    # Если цифры, меняем переменную на 0. Иначе 0 попадет в строку
    for i in args:
        if isinstance(i, int) or isinstance(i, float):
            digitTrigger = True
    if digitTrigger == True:
        rez = 0
        
    for i in args:
        try:
            if isinstance(i, str):
                if isinstance(rez, float):
                    print(err)
                    exit()
                rez += i
            if isinstance(i, int) or isinstance(i, float):
                if isinstance(rez, str):
                    print(err)
                    exit()
                rez = float(rez)
                rez += i
            if isinstance(i, list):
                if isinstance(rez, str) and len(rez) != 0:
                    print(err)
                    exit()
                rez = list(rez)
                rez.append(i)
        except TypeError:
            print(err)
            exit()
    return rez

print('Сумма чисел 4 и 9 =', sum(4, 9))
