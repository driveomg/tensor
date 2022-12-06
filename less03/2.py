import math
#Добавим возможность движения по диагонаоли

siny = math.sin(math.radians(45))
cosx = math.cos(math.radians(45))

x = float(0)
y = float(0)


while True:
    print(f'''Вычисление координат объекта по направлению и шагу.
Для выхода из программы ввиде "Стоп" в любом поле ввода.
Угол диагоналей = 45°
Текущие коринаты: X = {round(x, 5)}  Y = {round(y, 5)}''')

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
        vv = ['A','B','C','D','E','F','G','H','a','b','c','d','e','f','g','h']

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
        l = input("Введите шаг: ")
        if l == "стоп" or l == 'Стоп':
            exit()
            
        if l.isdigit() == True:
            l = float(l)       
        else:
            print('Шаг должен быть числом и быть больше нуля')
            continue
        if l > 0:
            b = True
        else:   print('Шаг должен быть числом и быть больше нуля')

    if v == ('A') or v == ('a'):
        x = x + (l * -cosx)
        y = y + (l * siny)
    elif v == ('B') or v == ('b'):
        x = x + 0
        y =y + l
    elif v == ('C') or v == ('c'):
        x = x + (l * cosx)
        y = y + (l *  siny)
    elif v == ('D') or v == ('d'):
        x = x + -l
        y = y + 0
    elif v == ('E') or v == ('e'):
        x = x + l
        y = y + 0
    elif v == ('F') or v == ('f'):
        x = x + (l * -cosx)
        y = y + (l * -siny)
    elif v == ('G') or v == ('g'):
        x = x + 0
        y =y + -l
    elif v == ('H') or v == ('h'):
        x = x + (l * cosx)
        y =y + (l * -siny)


   
