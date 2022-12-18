# Знакомство с библиотекой OS

import os

print('Имя ОС:')
print(os.name)
print(os.system('hostnamectl'))
print('Текущий пользователь:')
print(os.getlogin())
print(os.system('whoami'))
print('Файлы в текущей директории:')
print(os.listdir(path="."))
print(os.system('ls -la'))