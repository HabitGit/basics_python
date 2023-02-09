class Cat:
    name = None
    age = None
    IsHappy = None

    def set_data(self, name, age, IsHappy):
        self.name = name
        self.age = age
        self.IsHappy = IsHappy
    def get_data(self):
        print(self.name, 'age:', self.age, '.Happy:', self.IsHappy)


cat1 = Cat()
cat1.set_data('Barsik', 3, True)

cat2 = Cat()
cat2.set_data('Koten', 2, False)

cat1.get_data()
cat2.get_data()