# Пузырьеовая сортировка

from random import randint

print('Сортировка строки со случайными значениями(-100,100) заданной пользователем длинны')
l = input('Введите количество цифр в строке: ')

#Минимальная валидация ввода
try:
    l = int(l)               
except:
    print('Введенное значение должно быть целым числом.')
    exit()
if l <= 0:
    print('Введенное значение должно быть больше нуля.')
    exit()

#Вычисления
list = []
for i in range(l):
    list.append(randint(-100, 100))
print(f'Исходная строка:\n{list}')

c = 0
for run in range(l - 1):
    for i in range(l - 1 - run):
        if list[i] > list[i + 1]:
            c += 1
            buf = list[i + 1]
            list[i + 1] = list[i]
            list[i] = buf

print(f'Отсортированная по возрастанию строка\n{list}')
print(f'Количество перестановок {c}')


