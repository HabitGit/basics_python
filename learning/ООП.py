class Building: #Класс родитель
    year = None
    city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print('Year:', self.year, '.City:', self.city)


class School(Building): # Дочерний класс, наследует функции класса родитель
    pupils = 0

    def __init__(self, pupils, year, city):
        super(School, self).__init__(year, city) # Обращение к классу родитель через super()
        self.pupils = pupils

    def get_info(self): #Полиморфизм
        super().get_info() # Обращение к классу родитель через super
        print('Pupils', self.pupils)

class House(Building):
    pass

class Shop(Building):
    pass

school = School(100, 2000, "Moscow")
school.get_info()
house = House(2000, 'Moscow')
shop = Shop(2000, 'Moscow')
shop.get_info()