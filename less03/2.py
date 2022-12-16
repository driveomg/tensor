""" Cкрипт для движения персонажа влево, вправо, вверх и вниз, 
по диагонали по координатам x и y по координатной оси.
"""

import math

# Задим константы sin и cos для диагоналей 
siny = math.sin(math.radians(45))
cosx = math.cos(math.radians(45))

x = float(0)
y = float(0)

#Наглядный ввод данных и валидация
while True:
    print(f'Вычисление координат объекта по направлению и шагу.')
    print('Для выхода из программы ввиде "Стоп" в любом поле ввода.')
    print('Угол диагоналей = 45°')
    print(f'Текущие коринаты: X = {round(x, 5)}  Y = {round(y, 5)}')

    print(r''' 
     A\  B|  C/
       \  |  /
        \ | /
   D------0------E
        / | \
       /  |  \
     F/  G|  H\ ''')

    a = False
    while a != True:
        v = input("Введите вектор: ")
        vv = ['A', 'B', 'C', 'D', 
              'E', 'F', 'G', 'H', 
              'a', 'b', 'c', 'd', 
              'e', 'f', 'g', 'h'
              ]

        for i in vv:
            if v == i:
                a = True
                break
        if v == "стоп" or v == 'Стоп':
            exit()
        if a == False:
            print('Введный вектор не найден') 

    b = False
    while b != True:    
        t = input("Введите шаг: ")
        if t == "стоп" or t == 'Стоп':
            exit()
            
        if t.isdigit() == True:
            t = float(l)       
        else:
            print('Шаг должен быть числом и быть больше нуля')
            continue
        if t > 0:
            b = True
        else:   print('Шаг должен быть числом и быть больше нуля')

    if v == ('A') or v == ('a'):
        x = x + (t * -cosx)
        y = y + (t * siny)
    elif v == ('B') or v == ('b'):
        x = x + 0
        y = y + t
    elif v == ('C') or v == ('c'):
        x = x + (t * cosx)
        y = y + (t * siny)
    elif v == ('D') or v == ('d'):
        x = x + -t
        y = y + 0
    elif v == ('E') or v == ('e'):
        x = x + t
        y = y + 0
    elif v == ('F') or v == ('f'):
        x = x + (t * -cosx)
        y = y + (t * -siny)
    elif v == ('G') or v == ('g'):
        x = x + 0
        y = y + -t
    elif v == ('H') or v == ('h'):
        x = x + (t * cosx)
        y = y + (t * -siny)


   
