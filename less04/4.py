"""Игровой интверь с возможность добавлять/убирать предметы.
Введено ограничение по весу.
"""

DB = {
    'Меч': 6, 'Молот': 8, 'Секира': 6, 
    'Кинжал': 1, 'Арбалет': 4, 'Лук': 2,
    'Щит': 5, 'Аптечка':1, 'Вода': 1
    }
D = {
    'Меч': 6, 'Молот': 8, 'Секира': 6,
    'Кинжал': 1, 'Арбалет': 4, 'Лук': 2,
    'Щит': 5, 'Аптечка':1, 'Вода': 1
    }

inv = {}
while True:
    print('Доступный инвентарь \nПредмет : Вес')
    for key, value in D.items():
        print(key, ":", value,)
    
    print('\n\nВаш текущий рюкзак(Он выдержит не более 15 кг):')
    print('/~~~~~~~~~~~~~~~~~~~~~~~~\ ')
    for key, value in inv.items():
        print(key, ":", value)
    print('Вес: ', sum(inv.values()), 'кг')
    print('\~~~~~~~~~~~~~~~~~~~~~~~~/ \n')
    print('Доступные действия:')
    print('Положить в рюкзак(+) | Убрать из рюкзака(-)')

    action = str(input('Введите действие: '))

    if action == "+" :
        item = input('Введите предмет: ')
        if D.get(item) != None:
            if (sum(inv.values()) + D.get(item)) > 15:
                print('Вес превышен! Вы не можете больше ничего унести, \
                       рюкзак нужно разгрузить\n\n')
                continue
            else:

                           
                inv[item] = D.get(item)
                D.pop(item)

                
    elif action == '-':
        item = input('Введите предмет: ')
        if DB.get(item) != None:
            D[item] = inv.get(item)           
            print('Рюкзак похудел на ', inv.pop(item))         

    