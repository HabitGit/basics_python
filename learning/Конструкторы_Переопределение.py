class Cat:
    name = None
    age = None
    isHappy = None

    # def __init__(self, name, age, isHappy):
    #     self.name = name
    #     self.age = age
    #     self.isHappy = isHappy

    def __init__(self, name, age, isHappy):
        self.set_data(name, age, isHappy)
        self.get_data()

    def set_data(self, name = None, age = None, isHappy = None):
          self.name = name
          self.age = age
          self.isHappy = isHappy

    def get_data(self):
          print(self.name, 'age:', self.age, '.Happy:', self.isHappy)


cat1 = Cat("Barsik", 2, True)
cat1.set_data("John", 2,)
#cat1.set_data('Barsik', 3, True)

cat2 = Cat("Bicho", 3, False)
#cat2.set_data('Koten', 2, False)

# cat1.get_data()
# cat2.get_data()