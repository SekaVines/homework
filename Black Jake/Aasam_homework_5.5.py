class TimeDesk:
    def __init__(self, second):
        self.second = second


def SecondConverter(x):
    d = int(x / 86400)
    x -= (d * 86400)
    h = int(x / 3600)
    x -= (h * 3600)
    m = int(x / 60)
    x -= (m * 60)
    s = x
    print("Your input is equal to ", d, " days, ", h, " hours, ", m, " minutes, and ", s, "seconds.")

    def __str__(self):
        return f'Second: {self.second}'


SecondConverter(int(input("Your number:")))


class Chocolate:
    def __init__(self, cocoa, sugar, milk):
        self.cocoa = cocoa
        self.sugar = sugar
        self.milk = milk

    @classmethod
    def Changes(cls, sugar):
        changes_1 = cls(sugar='sugar substitute')
        return changes_1

    @staticmethod
    def portions():
        dose = 'dye' + 'chemicals'
        return dose

    @property
    def milk_chocolate_structure(self):
        milk_chocolate = self.cocoa + self.milk
        return milk_chocolate

    @milk_chocolate_structure.setter
    def milk_chocolate_structure(self, milk_chocolate):
        self.cocoa, self.milk = milk_chocolate.split

    @milk_chocolate_structure.deleter
    def milk_chocolate_structure(self):
        self.cocoa = None
        self.milk = None
        print('milk_chocolate_structure deleted!')

    def __str__(self):
        return f'Cocoa: {self.cocoa}\n' \
               f'Sugar: {self.sugar}\n' \
               f'Milk: {self.milk}'


chocolate_1 = Chocolate(cocoa='Cocoa',
                        sugar='Sugar',
                        milk='Milk')
print(chocolate_1)
chocolate_1.cocoa = 'CocoaPowder,  '
print(chocolate_1.milk_chocolate_structure)
del chocolate_1.milk_chocolate_structure
print(chocolate_1.milk_chocolate_structure)

