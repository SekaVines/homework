class Wizard:
    def __init__(self, name, ticket):
        self.name = name
        self.ticket = ticket

    def __add__(self, other):
        print('1. File ball')
        print('1. Freeze spell')
        if self.ticket == 1:
            summary = other + self.ticket
            return summary
        elif self.ticket == 2:
            summary = other * self.ticket
            return summary
    def __len__(self):
        return len(self.name)

    def __str__(self):
        return f'{self.name}, {self.ticket}'

wiz = Wizard(name='Gendalf', ticket=2)
print(wiz.__add__(200))
print(wiz.__len__())