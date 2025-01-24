class Cat:
    def meow(self):
        print('Гав!')

    name = 'Барсик'
    hp = 9
    fuel = 100

cat = Cat()
print(cat.name)
cat.name = 'Мухтар'
print(cat.name)
print(cat.fuel)
cat.meow()