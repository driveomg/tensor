import math
#Ввод и валидация
print("Введите два числа: ")
def x_valid():
    while True:
        try:
            zz0 = input("X =  ")
            zz1 = float(zz0.replace(',','.'))
            return zz1
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число")
x = x_valid()

def y_valid():
    while True:
        try:
            vv0 = input("Y =  ")
            vv1 = float(vv0.replace(',','.'))
            return vv1
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число")
y = y_valid()
#Вычисления

print('------------------------------------------------')
print(f'{x} + {y} = {x+y}')
print(f'{x} - {y} = {x-y}')
print(f'{x} X {y} = {round(x*y,5)}')
print(f'{x} / {y} = {round(x/y,5)}')
print(f'{x} в степени {y} = {round(x**y,5)}')  
print(f'{x} разделить по модулю на {y} = {round(x%y,5)}')  
print(f'Целочисленное деление {x} на {y} = {round(x//y,5)}')  
print('------------------------------------------------')