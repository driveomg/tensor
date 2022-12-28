# Проверка вводимого пароля

import getpass

def check(a):
    """ Фукнция проверят пароль согласно условиям """
    chk = True
    if len(a) < 6:       
        chk = False
    r = True    
    for i in a:                     
        if i.isdigit() == True:
            r = False
            break                                         
    if r == True:
        chk = False
    if a.isdigit() == True:        
        chk = False
    notpassword = a.lower()                 
    if notpassword.find('password') != -1:
        chk = False
    return  chk 

# a = getpass.getpass('Введите пароль: ')
# if check(a) == False:
#     print('Пароль не соответствует требованиям:')
#     print('- Должен быть не менее 6 символов;')
#     print('- Должен содержать хотя бы одну цифру;')
#     print('- Не должен состоять только из цифр;')
#     print('- Не должен содержать слово “password” в любом регистре.')
# else:
#     print('Пароль успешно принят.')
