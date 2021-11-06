class animal:
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Age: {self.age}' \
                f'Colour: {self.colour}'

class Zoo(animal):
    def __init__(self, cell, meal, name, age, colour):
        super().__init__(name, age, colour)
        self.cell = cell
        self.meal = meal

    def they_can_dance(self):
        return 'dance'

    def __str__(self):
        return f'Cell: {self.cell}\n' \
                f'Meal: {self.meal}'


class Zoo_show(Zoo):
    def __init__(self, cell, meal, name, age, colour):
        super().__init__(cell, meal, name, age, colour)
def ticket(self, cost):
    ticket_cost = 40
    summary = ticket_cost + cost
    print(summary)
a = Zoo_show(cell='big', meal='meat', name='tiger', age=2, colour='black and orange')
print(a)
