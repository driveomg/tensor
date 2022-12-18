# Создание матрицы со случайными значение и транспонирование её. 

import random
import numpy

normMatrix = numpy.random.randint(10, size=(3,3))
print(f'Матрица 3х3:\n{normMatrix}\n')
transpMatrix = normMatrix.transpose()
print(f'Транспонированная матрица 3х3:\n{transpMatrix}')



