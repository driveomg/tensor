Red = (255, 0, 0)
Pink = (255, 192, 203)
Orange = (255, 165, 0)
Yellow = (255, 255, 0)
Purple = (128, 0, 128)
Brown = (165, 42, 42)
Black = (0, 0, 0)
White = (255, 255, 255)
Green = (0, 128, 0)
D = {'Красный': Red, 'Розовый': Pink, 'Оранжевый': Orange, 'Желтый': Yellow, 'Пурпурный': Purple, 'Коричневый': Brown, 'Черный': Black, 'Белый':White, 'Зеленый': Green}

print('Цвет : RGB-код')
for key, value in D.items():
    print(key, ":", value)


