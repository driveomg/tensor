""" Ввод имени отчества, приветсвие по ИО """

a, *b = input('Пожалуйста, введите Ваше имя: ').split()
bb = ''.join(b)
bbl = len(bb)

# Валдиация и вывод

if bbl == 0:
    if a.isalpha():
        print(f'{a.title()}, здравствуйте!')
    else:
        print("Похоже, что Вы ввели что-то другое")
else:
    if a.isalpha():
        if bb.isalpha():
            print(f'{a.title()} {bb.title()}, здравствуйте!')
        else:
            print("Похоже, что Вы ввели что-то другое")
    else:
        print("Похоже, что Вы ввели что-то другое")
