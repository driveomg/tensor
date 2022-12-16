# Вычисление числа Фибоначчи(рекурсия)

def fib(n):
    """ Функция рекурсивно вызывает саму себя пока не дойдет до значений n-1=2 и  n-2=1 """

    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)
      
 
while True:
    try:
        n = int(input('Введите номер числа в последовательности Фибоначчи: '))
        if n < 0:
            raise ValueError
        break
    except ValueError:
        print('Ошибка. Введите целое не отрицательное число')
print('Значение числа в послежовательности:', fib(n))