import random
from random import randint

n1 = random.randint(9,15)
n2 = random.randint(9,15)

list1 = set()
for x in range(n1):
    list1.add(random.randint(1,30))

list2 = set()
for x in range(n2):
    list2.add(random.randint(1,30))

print('Генератор пары случайных наборов чисел запущен.')
print(f'Первый набор:\n{list1}')
print(f'Второй набор:\n{list2}\n')
print(f'Элементы, которые входят одновременно в оба набора:\n{list1.intersection(list2)}') 
print(f'Элементы, которые входят только в первый набор:\n{list1.difference(list2)}') 
print(f'Элементы, которые входят только в первый набор:\n{list2.difference(list1)}') 
print(f'Элементы, которые входят в первое или во второе, но не в оба из них одновременно:\n{list2.symmetric_difference(list1)}') 

