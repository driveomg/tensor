"""
Написать функцию. Для неё написать декораторы для следующего функционала:
    ◦ логирование выполнения функции;
    ◦ время выполнения функции;
"""



from datetime import datetime

def dec_log(func):
    """
    Логирование функции с двумя аргументами 
    в файл log.txt
    """
    def wrapper(arg1, arg2):
        with open('log.txt', 'w') as wr:
            t1= datetime.now()
            a = str(func(arg1, arg2))
            wr.write(f'[+] {datetime.now()} ::: Start logging\n')
            wr.write(f'[+] {datetime.now()} ::: arg1: {arg1} , arg2: {arg2}\n')
            wr.write(f'[+] {datetime.now()} ::: Function launch\n')
            wr.write(f'{a}\n')
            wr.write(f'[+] {datetime.now()} ::: Function end\n')
            t2 = datetime.now() - t1
            wr.write(f'[+] {datetime.now()} ::: Elapsed time {t2}')
    return wrapper



@dec_log
def centAcc(v, r):
    """Расчет центростремительного ускорения"""
    try:
        v = float(v)
        r = float(r)
    except ValueError:
        print('Incorrect value V or R')
        exit()
    a_digit = round((v**2 / r), 3)
    a_str = (f'Центростремительное ускорение = {a_digit} м/с')
    return a_str

centAcc(10, "24")
 
