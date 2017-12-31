class CocaCola:
    calories = 140
    sodium = 45
    total_carb = 39
    caffeine = 34
    ingredients = [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
        'Caffeine'
    ]

    def __init__(self, logo_name):
        self.local_logo = logo_name

    def drink(self):
        print('You get {} cal energy!'.format(self.calories))


# coke_for_me = CocaCola('可口可乐')
# coke_for_me.drink()
# print(coke_for_me.local_logo)


class CaffeineFree(CocaCola):
    caffeine = 0
    ingredients = [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color'
    ]


coke_a = CaffeineFree('CocaCola-FREE')


# coke_a.drink()


class TestA:
    attr = 1
    def __init__(self):
        self.attr = 42


obj_a = TestA()
obj_b = TestA()

# obj_a.attr =42
# print(obj_a.attr)
# print(obj_b.attr)
# print(TestA.attr)
print(TestA.__dict__)
print(obj_a.__dict__)

obj1 = 1
obj2 = 'String!'
obj3 = []
obj4 = {}

print(type(obj1),type(obj2),type(obj3),type(obj4))
