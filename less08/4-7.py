"""
Написать функцию. Для неё написать декораторы для следующего функционала:
    ◦ замедлить выполнение кода. Ограничить частоту вызова функции.
"""



import random 
import time


try:
    billet = int(input('Введите номер билет(0-20): '))   
except ValueError:
    print('Билет должен быть целым числом от 0 до 20')
    exit()
if billet < 0 or billet > 20:
    print('Билет должен быть целым числом от 0 до 20')
    exit()

    
def slow(func):
    """Декоратор замедления с частотой 1 раз в 0.3 сек."""   
    def wrapper(n):
        time.sleep(0.3)
        return func(n)
    return wrapper


@slow
def lotoFront(n):
    """Лотерея"""
    print(f'Число в билете {billet}, выпало число {n}')
    if n == billet:
        print("Ваш приз - Автомобиль!")       
        exit()
    else:
        lotoFront(random.randint(0, 20))
        

lotoFront(random.randint(0, 20))







