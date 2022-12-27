"""
Написать класс “Student”, который наследует класс human,
у которого среди прочих признаков есть “Количество сданных дз”.
"""


class Human:
        "Человек"
        def __init__(self, age, weight, height, citizenship):
                self.age = age
                self.weight = weight
                self.height = height
                self.citizenship = citizenship

class Student(Human):
        """Студент"""
        def __init__(
                self, age, weight, height, citizenship, 
                course, GPA, name, hwDone
                    ):
                super().__init__(age, weight, height, citizenship)
                self.course = course
                self.GPA = GPA
                self.name = name
                self.hwDone = hwDone

Igor = Student(19, 81, 180, 'РФ', 2, 4.5, 'Игорь', 3)
Ivan = Student(21, 70, 175, 'Белоруссия', 4, 4.8, 'Иван', 5)
Anton = Student(19, 59, 166, 'РФ', 1, 3.5, 'Антон', 6)
Sergey = Student(18, 79, 178, 'Казахстан', 1, 5, 'Сергей', 5)
Vladimir = Student(20, 79, 171, 'РФ', 2, 4.9, 'Владимир', 4)
Vadim = Student(22, 69, 170, 'РФ', 3, 3.7, 'Вадим', 11)
Dmitriy = Student(24, 66, 169, 'Украина', 5, 4.1, 'Дмитрий', 1)
Nikita = Student(17, 84, 182, 'РФ', 1, 4.6, 'Никита', 7)
Alexandr = Student(20, 90, 189, 'РФ', 2, 4, 'Александр', 9)
Alexey = Student(22, 66, 174, 'Белоруссия', 4, 3.9, 'Алексей', 4)

print(f'Средний балл студента {Ivan.name} составляет {Ivan.GPA}')
print(f'Студент {Igor.name} имеет гражданство {Igor.citizenship}.')
GPAstud = []
GPAstud.append(Igor.GPA)
GPAstud.append(Ivan.GPA)
GPAstud.append(Anton.GPA)
GPAstud.append(Sergey.GPA)
GPAstud.append(Vladimir.GPA)
GPAstud.append(Vadim.GPA)
GPAstud.append(Dmitriy.GPA)
GPAstud.append(Nikita.GPA)
GPAstud.append(Alexandr.GPA)
GPAstud.append(Alexey.GPA)

i = 0
summ = 0
for n in GPAstud:
        i += 1
        summ += n

print(f'Средний балл всех студентов: {summ / i}')