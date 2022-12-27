"""
Перегрузить операторы сравнения так, 
чтобы студенты сравнивались по количеству сданных ими дз
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

        def __lt__(st1, st2):
            """Перегрузка оператора 'строго меньше' """
            stud1 = st1.hwDone
            stud2 = st2.hwDone
            return stud1 < stud2    

        def __le__(st1, st2):
            """Перегрузка оператора 'меньше или равно' """
            stud1 = st1.hwDone
            stud2 = st2.hwDone
            return stud1 <= stud2   

        def __eq__(st1, st2):
            """Перегрузка оператора 'равно' """
            stud1 = st1.hwDone
            stud2 = st2.hwDone
            return stud1 == stud2   
        
        def __ne__(st1, st2):
            """Перегрузка оператора 'не равно' """
            stud1 = st1.hwDone
            stud2 = st2.hwDone
            return stud1 != stud2   
        
        def __gt__(st1, st2):
            """Перегрузка оператора 'строго больше' """
            stud1 = st1.hwDone
            stud2 = st2.hwDone
            return stud1 > stud2   
        
        def __ge__(st1, st2):
            """Перегрузка оператора 'больше или равно' """
            stud1 = st1.hwDone
            stud2 = st2.hwDone
            return stud1 >= stud2   




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

print(Igor < Dmitriy) 
print(Igor > Dmitriy)
print(Ivan != Sergey)
print(Vladimir >= Alexey)
print(Nikita == Alexandr)
print(Vadim <= Alexandr)
