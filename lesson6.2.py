class Human:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f'{self.first} + {self.last}.@gmail.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def __str__(self):
        return f'{self.first} {self.last}'

h = Human(first='Liz', last='Wizardo')

print(h)
print(h.fullname)
h.first = 'dfgdf'
print(h.fullname)