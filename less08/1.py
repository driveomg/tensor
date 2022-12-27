"""  
Написать класс “animals” (животные), который включает общие признаки и поведения животных. 
От “animals” наследовать класс “mammals” (млекопитающие), который включает общие признаки 
и поведения млекопитающих. 
От “mammals” наследовать “human” (человек), “cat”(кот), “dog”(собака), 
у каждого свои признаки и поведения.
"""


class Animals:
    """Животные - составляющие домена Эукариоты."""
    # постоянные составляющие 
    move = True
    organSystem = ('Нерваная система', 'Пищеварительная система')
    synthesis = True
    bodySymmetry = True
    immobility = False
    Photosynthesis = False

    # Изменяемые атрибуты
    def __init__(self, name, age, weight, color):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
   
    
        
       
class Mammals(Animals):
    """Млекопитающие - двусторонне-симметричные, вторичноротые, хордовые."""
    # Постоянные состовляющие
    spine = True
    liveBirth = True
    wool = True
    teeth = True
    coldBlooded = False

    # Изменяемые атрибуты
    def __init__(self, name, age, weight, color, temp, heart):
        super().__init__(name, age, weight, color)
        self.temp = temp
        self.heart = heart
    
    def wiki(self):
        print('Млекопитающие - двусторонне-симметричные, вторичноротые, хордовые.')

# Наследуем экземпляры класса. Из задания не совсем понял, 
# наследуем классы(human, cat, dog) или экземпляры класса. 
# Выполнил задание через экземпляры.
human = Mammals('Иван', 33, 80, 'Смуглый', 36.6, 'Четырехкамерное')
cat = Mammals('Пушок', 1, 3, 'Черно-белый', 38, 'Четырехкамерное')
dog = Mammals('Хром', 5, 10, 'Бежевый', 37.8, 'Четырехкамерное')
human.socialization = True
human.speech = True
cat.life = 9
dog.level_of_devotion = 'максимальный'

if human.move == True:
    print(f'{human.name} может двигаться.')
if human.wool == True:
    print(f'{human.name} имеет волосы на теле.')
if human.speech == True:
    print(f'{human.name} может разговарить.')

if cat.synthesis == True:
    print(f'Кот {cat.name} может синтезировать вещества в организме.')
if cat.coldBlooded == False:
    print(f'Кот {cat.name} теплокровное животное.')
print(f'Кот {cat.name} имеет {cat.life} жизней')

if dog.immobility == False:
    print(f'Пес {dog.name} может передвигаться.')
if dog.spine == True:
    print(f'Пес {dog.name} имеет позвоночник.')
print(f'Пес {dog.name} имеет {dog.level_of_devotion} уровень преданности.')

human.wiki()

