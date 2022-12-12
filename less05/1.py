import getpass

def check(a):
    chk = True
    if len(a) < 6:       #Проверка на длинну
        chk = False

    r = True    
    for i in a:                     # Проверка на одну цифру
        if i.isdigit() == True:
            r = False
            break                                         
    if r == True:
        chk = False

    if a.isdigit() == True:        #Проверка только на цифры
        chk = False

    notpassword = a.lower()                 #Проверка на 'password' в пароле
    if notpassword.find('password') != -1:
        chk = False

    return  chk 

a = getpass.getpass('Введите пароль: ')
if check(a) == False:
    print('''Пароль не соответствует требованиям:
- Должен быть не менее 6 символов;
- Должен содержать хотя бы одну цифру;
- Не должен состоять только из цифр;
- Не должен содержать слово “password” в любом регистре.'''   )
else:
    print('Пароль успешно принят.')
