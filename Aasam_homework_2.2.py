class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}\n' \
                f'Age: {self.age}\n'

child_1 = Child(name='Azat',
                age=12)
print(child_1)

class Father(Child):
    def __init__(self, name, age, experience, understanding):
        super().__init__(name, age)
        self.experience = experience
        self.understanding = understanding

    def __str__(self):
        return super(Father, self).__str__() + f'\nExperience : {self.experience}\n' \
                                                f'Understandig : {self.understanding}'
father_1 = Father(name='Azamat',
                  age=45,
                  experience='have',
                  understanding='understanding about life')
print(father_1)

class Grandfather(Father):
    def __init__(self, name, age, experience, understanding, knows_much, condition):
        super().__init__(name, age, experience, understanding)
        self.knows_much = knows_much
        self.condition = condition

    def __str__(self):
        return super(Grandfather, self).__str__() + f'\nKnows_much : {self.knows_much}\n' \
                                                    f'Condition : {self.condition}'
Grandfather_1 = Grandfather(name='Zhumaly',
                            age=100,
                            experience='have',
                            understanding='the meaning of life',
                            knows_much='knows about life',
                            condition='old')
print(Grandfather_1)


class Soldat:
    def __init__(self, name, age, attack):
        self.name = name
        self.age = age
        self.attack = attack
    def __str__(self):
        return f'Name: {self.name}\n' \
                f'Age: {self.age}\n' \
                f'Attack: {self.attack}\n'

class Sniper(Soldat):
    def __init__(self, name, age, attack):
        super().__init__(name, age, attack)

    def __str__(self):
        return super(Sniper, self).__str__()
sniper_1 = Sniper(name='sniper',
                  age=24,
                  attack='Стреляет с снайпера')
print(sniper_1)
