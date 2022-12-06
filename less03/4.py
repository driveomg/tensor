import math
import cmath


selector=input('Будут ли использоваться комплексные числа?(Да/Нет) ')
if selector =='Да' or selector =='да' or selector =='Yes' or selector =='yes' or selector =='+' :
    print('''Общие вид квадратного уравнения Ax² + Bx + C = 0 , где a ≠ 0
Введите коэфиценты(Пример: 1+5j)''')
    a=complex(input("A = "))
    b=complex(input("B = "))
    c=complex(input("C = "))
    if a == 0:
        print('Введн некорректный коэфицент. Коэфицент A не должен быть = 0.')
        exit()   
        
    if b==0:
        x =math.sqrt(-c / a)
        print(f'Уравнение имеет один корень \nX = {x}')
    else:
        d=b*b-4*a*c
        x1=(-b+cmath.sqrt(d))/(2*a)
        x2=(-b-cmath.sqrt(d))/(2*a)
        print(f'Дискриминант = {d}')
        print(f'Корни уравнения: \nX₁ = {x1}\nX₂ = {x2}')
       
else:
    print('''Общие вид квадратного уравнения Ax² + Bx + C = 0 , где a ≠ 0
    Введите коэфиценты''')
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
        
                            
