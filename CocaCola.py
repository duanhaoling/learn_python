class CocaCola:
    formula = ['caffeine', 'sugar', 'water', 'soda']
    it_taste = 'So good!'

    def __init__(self):
        self.local_logo = '可口可乐'
        for element in self.formula:
            print('Coke has {}'.format(element))

    def drink(self, how_much):
        if how_much == 'a sip':
            print('Cool~')
        if how_much == 'whole bottle':
            print('Headache!')


coke_for_China = CocaCola()
# coke_for_China.local_logo = "可口可乐"
coke_for_China.drink('a sip')
# print(coke_for_China.local_logo)
