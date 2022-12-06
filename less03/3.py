import math
while True:
    print('''Общие вид квадратного уравнения Ax² + Bx + C = 0 , где a ≠ 0
    Введите коэфиценты''')
#Ввод коэфицентов и валидация
    a0 = 0
    while a0 < 4 :    
            a = input("A = ")                    
            if a == ('0'):                
                print('Введн некорректный коэфицент. Коэфицент A не должен быть = 0.')
                exit() 
            elif a.isdigit() == True:
                a = float(a) 
                a0 += 4                        
            elif a0 == 3:               
                print('Введн некорректный коэфицент. Уравнение не сможет быть решено.')
                exit()   
            else:
                print('Коэфицентом может быть только число')
                a0 += 1
                continue

    b0 = 0
    while b0 < 4 :    
            b = input("B = ")                    
            if b.isdigit() == True:
                b = float(b) 
                b0 += 4   
            elif b0 == 3:
                    print('Введн некорректный коэфицент. Уравнение не сможет быть решено.')
                    exit()   
            else:
                print('Коэфицентом может быть только число')
                b0 += 1
                    

    c0 = 0
    while c0 < 4 :    
            c = input("C = ")                    
            if c.isdigit() == True:
                c = float(c) 
                c0 += 4   
            elif c0 == 3:
                    print('Введн некорректный коэфицент. Уравнение не сможет быть решено.')
                    exit()   
            else:
                print('Коэфицентом может быть только число')
                c0 += 1
                                            

#Вычисление
    d = b**2 - (4 * a * c)
    print(f'Дискриминант = {d}')
    if d >= 0:
        x1 = (-b + math.sqrt(b**2 - (4 * a * c))) / (2 * a)
        x2 = (-b - math.sqrt(b**2 - (4 * a * c))) / (2 * a)
        if x1 == x2:
            print(f'Уравнение имеет один корень \nX = {round(x1,5)}')
        else:
            print(f'Корни уравнения: \nX₁ = {round(x1,5)}\nX₂ = {round(x2,5)}')
        
    else: 
        print('Квадратное уравнение не имеет корней.')

    q = input('Решим еще одно уравнение?  ')
    if q == ('да') or q == ('Да') or q == ('Y') or q == ('yes') or q == ('Yes') or q == ('+'):
        continue
    else:
        exit()

        