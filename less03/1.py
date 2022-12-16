""" Cкрипт для движения персонажа влево, вправо, вверх и вниз, 
по диагонали по координатам x и y по координатной оси. 
"""

import math

siny = math.sin(math.radians(45))
cosx = math.cos(math.radians(45))

#Наглядный ввод данных и валидация 
print(r'''Вычисление координат объекта по направлению и шагу.
    Угол диагоналей = 45°
    Начальные координаты по осям X Y (0,0)

    A\  B|  C/
      \  |  /
       \ | /
  D------0------E
       / | \
      /  |  \
    F/  G|  H\ ''')
v = input("Введите вектор: ")
vv = ['A', 'B', 'C', 'D', 
      'E', 'F', 'G', 'H', 
      'a', 'b', 'c', 'd', 
      'e', 'f', 'g', 'h'
      ]

for i in vv:
    if v == i:
        k = True
        break
    else: 
        k = False
if k == False:
    print('Введный вектор не найден') 
    exit()

l = float(input("Введите шаг: "))
if l <= 0:
    print('Размер шага должен быть больше нуля.')
    exit()

if v == ('A') or v == ('a'):   
    x = l * -cosx
    y = l * siny
elif v == ('B') or v == ('b'):
    x = 0
    y = l
elif v == ('C') or v == ('c'):
    x = l * cosx
    y = l *  siny
elif v == ('D') or v == ('d'):
    x = -l
    y = 0
elif v == ('E') or v == ('e'):
    x = l
    y = 0
elif v == ('F') or v == ('f'):
    x = l * -cosx
    y = l * -siny
elif v == ('G') or v == ('g'):
    x = 0
    y = -l
elif v == ('H') or v == ('h'):
    x = l * cosx
    y = l * -siny


print(f'''Новые координаты:
X = {round(x,5)}
Y = {round(y,5)}
''')