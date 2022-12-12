#0, 1, 1, 2, 3, 5, 8, 13...  Нулевое значение ряда = 0
def func(n):
    """ Функция рекурсивно вызывает саму себя пока не дойдет до значений n-1=2 и  n-2=1 """
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return func(n-1) + func(n-2)
    
    
 
while True:
    try:
        n = int(input('Введите номер числа в последовательности Фибоначчи: '))
        if n < 0:
            raise ValueError
        break
    except ValueError:
        print('Ошибка. Введите целое не отрицательное число')
print('Значение числа в послежовательности:', func(n))