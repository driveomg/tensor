""" Перобразование ссписка строк в список байт кодов. Обратная функция"""


a1 = list(['Москва', 'Питер', 'Новгород', 'Ярославль','Тюмень','Сочи'])
a = list(['ABCxyz@', '146%'])
b1 = list([
         '1052 1086 1089 1082 1074 1072', '1055 1080 1090 1077 1088', 
         '1053 1086 1074 1075 1086 1088 1086 1076', 
         '1071 1088 1086 1089 1083 1072 1074 1083 1100', 
         '1058 1102 1084 1077 1085 1100', '1057 1086 1095 1080'
         ])
b = list([
         '1058 1077 1085 1079 1086 1088', '80 121 116 104 111 110',
         '50 32 1089 1090 1074 1086 1083 1072'
         ])


def convert(a):
    """Функция принимает на вход список из строк. 
    Возвращает список из байт кодов с разделителем пробел(для удобства чтения)"""

    sb = list()
    for i in a:              
        z = 0
        s = ''
        for n in i:           
            z += 1          
            s += str(ord(n)) + ' '                  
            if z == len(i):
                s = s[:-1]
                sb.append(s)            
    return sb

def deconvert(a):
    """функция принимает на вход список из байт кодов с разделителем пробел. 
    Зная нужный формат входа функцию легко изменить.
    Фунция возвращает список строк."""

    sb = list()
    for i in a:              
        z = len(i)
        l = i.split() 
        z = 0
        s = ''
        for n in l:
            z +=  1           
            s += str(chr(int(n)))  
            if z == len(l):
                sb.append(s)                        

    return sb

print(convert(a))
print(deconvert(b))        






