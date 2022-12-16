""" Скрипт принимает в файле in.txt последовательно тест и ключ шифрования, 
разделитель пробел, строки.
Результат: зашифрованная строка записывается в файл out.txt
"""


import os

with open('in.txt', encoding='utf8') as f:   
    dirt = f.read()

try:
    stroka = (dirt.split()[0])  
    key = (dirt.split()[1])      
except:
    print('Значение в файле in.txt некорректное')
    exit()


# Валидируем считанные строки. Если строка больше ключа, заполняем ключ нулями.
if len(stroka) < len(key):
    print('Строка меньше ключа. Длинна ключа сокращена')
elif len(stroka) > len(key):
    print('Строка больше ключа. Криптостойкость снижена.')
    key = key.zfill(len(stroka))
else: 
       print('Файл зашифрован')

#Заносим в список байт представление ключа 
try:
    key22 = list()
    for i in key.encode('Windows-1251'):
        key22.append(i)
except UnicodeEncodeError:
    print('Ошибка кодировки. Измените символы ключа')
    exit()

#Заносим в список байт представление строки
try:
    str11 = list()
    for g in stroka.encode('Windows-1251'):
        str11.append(g)
except UnicodeEncodeError:
    print('Ошибка кодировки. Измените символы строки')
    exit()

#Ксорим ключ и шифр
shfr = list()
for q in range(len(str11)):
    shfr.append((str11[q]^key22[q]))
    

#Записываем в файл зашифрованный файл 
with open('out.txt', 'w') as wr:
    wr.write(bytes(shfr).decode('Windows-1251'))
