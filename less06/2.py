import os
#Формат файла Input.txt:  C H O, где C - Углерод, H - Водород, О - Кислород. Числа записаны целые, через разделитель пробел.
#Вывод в файл Output.txt. Записывается число, без форматирования ввода для упрощения дальнейшего использования 
with open('Input.txt') as f:
    dirt = f.read()
    
#Записываем в переменные результат целочисленного деления согласно формуле  C2H5(OH)
try:
    C = int(dirt.split()[0]) // 2
    H = int(dirt.split()[1]) // 6
    O = int(dirt.split()[2])   
except:
    print('Значение в файле Input.txt некорректное')
    exit()

#Записываем в файл минимальное значение 
with open('Output.txt', 'w') as wr:
    wr.write(str(min(C, H, O)))