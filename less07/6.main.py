"Расчет значений(напряжение,ток, сопростивление) по закону Ома"
import om

while True:
    try:
        choice = str(input('Что требуется вычислить(I, R, U): '))
        if choice in 'I' or choice in 'i' or \
           choice in 'ш' or choice in 'Ш':
            R = float(input('R = '))
            U = float(input('U = '))
            print (f'Сила тока I = {om.tok(U, R)} A')       
        elif choice in 'R' or choice in 'r' or \
             choice in 'к' or choice in 'К':
            U = float(input('U = '))
            I = float(input('I = '))
            print(f'Сопротивление R = {om.rezist(U, I)} Ом')
        elif choice in 'U' or choice in 'u' or \
             choice in 'Г' or choice in 'г':
            I = float(input('I = '))
            R = float(input('R = '))
            print(f'Напряжение U = {om.volt(I, R)} V')
        else:
            print('Некорректный ввод.')
    except ValueError:
        print('Значение должно быть числом')